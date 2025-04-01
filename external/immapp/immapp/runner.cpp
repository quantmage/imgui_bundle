#include "immapp.h"

#ifdef IMGUI_BUNDLE_WITH_IMPLOT
#include "implot/implot.h"
#endif
#ifdef IMGUI_BUNDLE_WITH_IMPLOT3D
#include "implot3d/implot3d.h"
#endif
#ifdef IMGUI_BUNDLE_WITH_IMFILEDIALOG
#include "bundle_integration/ImFileDialogTextureHelper.h"
#endif

#ifdef IMGUI_BUNDLE_WITH_TEXT_INSPECT
#include "imgui_tex_inspect/imgui_tex_inspect.h"
#include "imgui_tex_inspect/backends/tex_inspect_opengl.h"
#endif
#include "hello_imgui/hello_imgui.h"
#include "hello_imgui/internal/functional_utils.h"
#undef IMGUI_BUNDLE_WITH_IMMVISION
#ifdef IMGUI_BUNDLE_WITH_IMMVISION
#include "immvision/immvision.h"
#endif

#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
std::function<void()> FnResetImGuiNodeEditorId; // may be bound from pybind_imgui_node_editor.cpp
void UpdateNodeEditorColorsFromImguiColors();
#endif

#include <chrono>
#include <cassert>
#include <filesystem>


// Private API used by ImGuiTexInspect (not mentioned in headers!)
namespace HelloImGui { std::string GlslVersion(); }


namespace ImmApp
{

    struct ImmAppContext
    {
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        std::optional<ax::NodeEditor::EditorContext *> _NodeEditorContext;
        ax::NodeEditor::Config _NodeEditorConfig;
#endif

#ifdef IMGUI_BUNDLE_WITH_TEXT_INSPECT
        ImGuiTexInspect::Context * _ImGuiTextInspect_Context = nullptr;
#endif
    };

    ImmAppContext gImmAppContext;

    // Only one instance of `Renderer` can exist at a time
    // ---------------------------------------------------
    static int gRendererInstanceCount = 0;
    static AddOnsParams gAddOnsParamsAtSetup;

    static void Priv_TearDown();


    static void Priv_Setup(HelloImGui::RunnerParams& runnerParams, const AddOnsParams& passedAddOnsParams)
    {
        gAddOnsParamsAtSetup = passedAddOnsParams;
        AddOnsParams& addOnsParams = gAddOnsParamsAtSetup; // We may modify those

        // Check if we are already running
#ifdef IMGUI_BUNDLE_BUILD_PYTHON
        // For python, we forgive the user for not calling TearDown() before calling Renderer()
        // since it might be due to a Python exception, which might be recoverable, if running
        // in a Python REPL, a notebook, or Pyodide.
        if (gRendererInstanceCount > 0)
        {
            printf("ImmApp: calling TearDown() prior to Setup (probable prior exception in Python).\n");
            Priv_TearDown();
        }
#else
        if (gRendererInstanceCount > 0)
        throw std::runtime_error("Only one instance of `ImmApp::Renderer` can exist at a time.");
#endif
        gRendererInstanceCount++;


        // create implot context if required
#ifdef IMGUI_BUNDLE_WITH_IMPLOT
        if (addOnsParams.withImplot)
            ImPlot::CreateContext();
#endif
        // create implot3d context if required
#ifdef IMGUI_BUNDLE_WITH_IMPLOT3D
        if (addOnsParams.withImplot3d)
            ImPlot3D::CreateContext();
#endif

#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        // create imgui_node_editor context if required
        if (addOnsParams.withNodeEditor || addOnsParams.withNodeEditorConfig.has_value())
        {
            addOnsParams.withNodeEditor = true;
            if (addOnsParams.withNodeEditorConfig.has_value())
                gImmAppContext._NodeEditorConfig = addOnsParams.withNodeEditorConfig.value();

            // Replace settings file name if default
            if (gImmAppContext._NodeEditorConfig.SettingsFile == "NodeEditor.json")
            {
                gImmAppContext._NodeEditorConfig.SettingsFile = NodeEditorSettingsLocation(runnerParams);
            }

            gImmAppContext._NodeEditorContext = ax::NodeEditor::CreateEditor(&gImmAppContext._NodeEditorConfig);
            ax::NodeEditor::SetCurrentEditor(gImmAppContext._NodeEditorContext.value());

            runnerParams.callbacks.BeforeExit = HelloImGui::SequenceFunctions(
                FnResetImGuiNodeEditorId,
                runnerParams.callbacks.BeforeExit
            );

            // Update node editor colors from imgui colors
            auto fnUpdateNodeEditorColorsFromImguiColors = [&]
            {
                if (addOnsParams.updateNodeEditorColorsFromImguiColors)
                    UpdateNodeEditorColorsFromImguiColors();
            };
            // Once at startup
            runnerParams.callbacks.SetupImGuiStyle = HelloImGui::SequenceFunctions(
                runnerParams.callbacks.SetupImGuiStyle,
                fnUpdateNodeEditorColorsFromImguiColors
            );
            // Once every frame. We choose a relatively unused callback to avoid
            // situations where a user would forget to chain the callbacks.
            runnerParams.callbacks.BeforeImGuiRender = HelloImGui::SequenceFunctions(
                runnerParams.callbacks.BeforeImGuiRender,
                fnUpdateNodeEditorColorsFromImguiColors
            );
        }
#endif

        // load markdown fonts if needed
        if (addOnsParams.withMarkdown || addOnsParams.withMarkdownOptions.has_value())
        {
            if (!addOnsParams.withMarkdownOptions.has_value())
                addOnsParams.withMarkdownOptions = ImGuiMd::MarkdownOptions();
            ImGuiMd::InitializeMarkdown(addOnsParams.withMarkdownOptions.value());

            runnerParams.callbacks.LoadAdditionalFonts = HelloImGui::SequenceFunctions(
                runnerParams.callbacks.LoadAdditionalFonts,
                ImGuiMd::GetFontLoaderFunction());
        }

#ifdef IMGUI_BUNDLE_WITH_IMFILEDIALOG
        ImFileDialogSetupTextureLoader();
#endif

#ifdef IMGUI_BUNDLE_WITH_TEXT_INSPECT
        if (addOnsParams.withTexInspect)
        {
            // Modify post-init: Init ImGuiTexInspect
            {
                auto fn_ImGuiTextInspect_Init = [&runnerParams, &addOnsParams](){
                    if (runnerParams.rendererBackendType == HelloImGui::RendererBackendType::OpenGL3)
                    {
                        ImGuiTexInspect::ImplOpenGL3_Init(HelloImGui::GlslVersion().c_str());
                        ImGuiTexInspect::Init();
                        gImmAppContext._ImGuiTextInspect_Context = ImGuiTexInspect::CreateContext();
                    }
                    else
                    {
                        addOnsParams.withTexInspect = false;
                        fprintf(stderr, "ImGuiTexInspect is only supported with OpenGL renderer!");
                    }
                };
                runnerParams.callbacks.PostInit = HelloImGui::SequenceFunctions(
                    fn_ImGuiTextInspect_Init,
                    runnerParams.callbacks.PostInit
                );
            }

            // Modify before-exit: DeInit ImGuiTexInspect
            {
                auto fn_ImGuiTextInspect_DeInit = [&addOnsParams](){
                    if (addOnsParams.withTexInspect)
                    {
                        ImGuiTexInspect::Shutdown();
                        ImGuiTexInspect::DestroyContext(gImmAppContext._ImGuiTextInspect_Context);
                        ImGuiTexInspect::ImplOpenGl3_Shutdown();
                    }
                };
                runnerParams.callbacks.BeforeExit = HelloImGui::SequenceFunctions(
                    fn_ImGuiTextInspect_DeInit,
                    runnerParams.callbacks.BeforeExit
                );
            }
        }
#endif

#ifdef IMGUI_BUNDLE_WITH_IMMVISION
        // Clear ImmVision cache, before OpenGl is uninitialized
        runnerParams.callbacks.BeforeExit = HelloImGui::SequenceFunctions(
            runnerParams.callbacks.BeforeExit,
            ImmVision::ClearTextureCache);
#endif
    }

    static void Priv_TearDown()
    {
        AddOnsParams& addOnsParams = gAddOnsParamsAtSetup;

        gRendererInstanceCount = 0;

#ifdef IMGUI_BUNDLE_WITH_IMPLOT
        if (addOnsParams.withImplot)
            ImPlot::DestroyContext();
#endif
#ifdef IMGUI_BUNDLE_WITH_IMPLOT3D
        if (addOnsParams.withImplot3d)
            ImPlot3D::DestroyContext();
#endif

#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        if (addOnsParams.withNodeEditor)
        {
            assert(gImmAppContext._NodeEditorContext.has_value());
            ax::NodeEditor::DestroyEditor(*gImmAppContext._NodeEditorContext);
            gImmAppContext._NodeEditorContext = std::nullopt;
        }
#endif

        if (addOnsParams.withMarkdown || addOnsParams.withMarkdownOptions.has_value())
            ImGuiMd::DeInitializeMarkdown();
    }

    void Run(HelloImGui::RunnerParams& runnerParams, const AddOnsParams& addOnsParams)
    {
        Priv_Setup(runnerParams, addOnsParams);
        HelloImGui::Run(runnerParams);
        Priv_TearDown();
    }

    void Run(const HelloImGui::SimpleRunnerParams& simpleParams, const AddOnsParams& addOnsParams)
    {
        HelloImGui::RunnerParams runnerParams = simpleParams.ToRunnerParams();
        Run(runnerParams, addOnsParams);
    }


    void Run(
        // HelloImGui::SimpleRunnerParams below:
        const VoidFunction& guiFunction,
        const std::string& windowTitle,
        bool windowSizeAuto,
        bool windowRestorePreviousGeometry,
        const ScreenSize& windowSize,
        float fpsIdle,

        // ImGuiBundle_AddOnsParams below:
        bool withImplot,
        bool withImplot3d,
        bool withMarkdown,
        bool withNodeEditor,
        bool withTexInspect,
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        const std::optional<NodeEditorConfig>& withNodeEditorConfig,
#endif
        const std::optional<ImGuiMd::MarkdownOptions> & withMarkdownOptions
    )
    {
        HelloImGui::SimpleRunnerParams simpleRunnerParams;
        simpleRunnerParams.guiFunction = guiFunction;
        simpleRunnerParams.windowTitle = windowTitle;
        simpleRunnerParams.windowSizeAuto = windowSizeAuto;
        simpleRunnerParams.windowRestorePreviousGeometry = windowRestorePreviousGeometry;
        simpleRunnerParams.windowSize = windowSize;
        simpleRunnerParams.fpsIdle = fpsIdle;

        AddOnsParams addOnsParams;
        addOnsParams.withImplot = withImplot;
        addOnsParams.withImplot3d = withImplot3d;
        addOnsParams.withMarkdown = withMarkdown;
        addOnsParams.withNodeEditor = withNodeEditor;
        addOnsParams.withTexInspect = withTexInspect;
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        addOnsParams.withNodeEditorConfig = withNodeEditorConfig;
#endif
        addOnsParams.withMarkdownOptions = withMarkdownOptions;

        Run(simpleRunnerParams, addOnsParams);
    }


    void RunWithMarkdown(
        // HelloImGui::SimpleRunnerParams below:
        const VoidFunction& guiFunction,
        const std::string& windowTitle,
        bool windowSizeAuto,
        bool windowRestorePreviousGeometry,
        const ScreenSize& windowSize,
        float fpsIdle,

        // ImGuiBundle_AddOnsParams below:
        bool withImplot,
        bool withImplot3d,
        bool withNodeEditor,
        bool withTexInspect,
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        const std::optional<NodeEditorConfig>& withNodeEditorConfig,
#endif
        const std::optional<ImGuiMd::MarkdownOptions> & withMarkdownOptions
    )
    {
        HelloImGui::SimpleRunnerParams simpleRunnerParams;
        simpleRunnerParams.guiFunction = guiFunction;
        simpleRunnerParams.windowTitle = windowTitle;
        simpleRunnerParams.windowSizeAuto = windowSizeAuto;
        simpleRunnerParams.windowRestorePreviousGeometry = windowRestorePreviousGeometry;
        simpleRunnerParams.windowSize = windowSize;
        simpleRunnerParams.fpsIdle = fpsIdle;

        AddOnsParams addOnsParams;
        addOnsParams.withImplot = withImplot;
        addOnsParams.withImplot3d = withImplot3d;
        addOnsParams.withMarkdown = true;
        addOnsParams.withNodeEditor = withNodeEditor;
        addOnsParams.withTexInspect = withTexInspect;
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        addOnsParams.withNodeEditorConfig = withNodeEditorConfig;
#endif
        addOnsParams.withMarkdownOptions = withMarkdownOptions;

        Run(simpleRunnerParams, addOnsParams);
    }

    float EmSize()
    {
        return HelloImGui::EmSize();
    }
    ImVec2 EmToVec2(float x, float y)
    {
        return HelloImGui::EmToVec2(x, y);
    }
    ImVec2 EmToVec2(ImVec2 v)
    {
        return HelloImGui::EmToVec2(v);
    }
    float EmSize(float nbLines)
    {
        return HelloImGui::EmSize(nbLines);
    }

    ImVec2 PixelsToEm(ImVec2 pixels)
    {
        return HelloImGui::PixelsToEm(pixels);
    }

    float  PixelSizeToEm(float pixelSize)
    {
        return HelloImGui::PixelSizeToEm(pixelSize);
    }


#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
    ax::NodeEditor::EditorContext* DefaultNodeEditorContext()
    {
        if (!gImmAppContext._NodeEditorContext.has_value())
            throw std::runtime_error("No current node editor context\n"
                                     "    Did you set with_node_editor_config when calling ImmApp::Run()?");
        return *gImmAppContext._NodeEditorContext;
    }

    ax::NodeEditor::Config* DefaultNodeEditorConfig()
    {
        return &gImmAppContext._NodeEditorConfig;
    }

    // NodeEditorSettingsLocation returns the path to the json file for the node editor settings.
    std::string NodeEditorSettingsLocation(const HelloImGui::RunnerParams& runnerParams)
    {
        std::string iniLocation = HelloImGui::IniSettingsLocation(runnerParams);
        // iniLocation is of the form path/to/your/app.ini
        // => we replace it with path/to/your/app_node_editor.json
        std::string jsonLocation = iniLocation;
        jsonLocation.replace(jsonLocation.size() - 4, 4, ".node_editor.json");
        return jsonLocation;
    }


    // HasNodeEditorSettings returns true if the json file for the node editor settings exists.
    bool HasNodeEditorSettings(const HelloImGui::RunnerParams& runnerParams)
    {
        std::string filename = NodeEditorSettingsLocation(runnerParams);
        if (filename.empty())
            return false;
        return std::filesystem::exists(filename);
    }

    // DeleteNodeEditorSettings deletes the json file for the node editor settings.
    void DeleteNodeEditorSettings(const HelloImGui::RunnerParams& runnerParams)
    {
        std::string filename = IniSettingsLocation(runnerParams);
        if (filename.empty())
            return;
        if (!std::filesystem::exists(filename))
            return;
        bool success = std::filesystem::remove(filename);
        IM_ASSERT(success && "Failed to delete ini file %s");
    }

#endif


// ========================= ManualRender ====================================================

namespace ManualRender  // namespace ImmApp::ManualRender
{
    // Enumeration to track the current state of the ManualRenderer
    enum class RendererStatus
    {
        NotInitialized,
        Initialized,
    };
    RendererStatus sCurrentStatus = RendererStatus::NotInitialized;

    // Changes the current status to Initialized if it was NotInitialized,
    // otherwise raises an error (assert or exception)
    void TrySwitchToInitialized()
    {
        if (sCurrentStatus == RendererStatus::Initialized)
            IM_ASSERT(false && "ImmApp::ManualRender::SetupFromXXX() cannot be called while already initialized. Call TearDown() first.");
        sCurrentStatus = RendererStatus::Initialized;
    }

    // Changes the current status to NotInitialized if it was Initialized,
    // otherwise raises an error (assert or exception)
    void TrySwitchToNotInitialized()
    {
        if (sCurrentStatus == RendererStatus::NotInitialized)
            IM_ASSERT(false && "ImmApp::ManualRender::TearDown() cannot be called while not initialized.");
        sCurrentStatus = RendererStatus::NotInitialized;
    }


    void SetupFromRunnerParams(const HelloImGui::RunnerParams& runnerParams, const AddOnsParams& addOnsParams)
    {
        TrySwitchToInitialized();
        HelloImGui::RunnerParams runnerParamsCopy = runnerParams;
        Priv_Setup(runnerParamsCopy, addOnsParams);
        HelloImGui::ManualRender::SetupFromRunnerParams(runnerParamsCopy);
    }

    void SetupFromSimpleRunnerParams(const HelloImGui::SimpleRunnerParams& simpleParams, const AddOnsParams& addOnsParams)
    {
        HelloImGui::RunnerParams runnerParams = simpleParams.ToRunnerParams();
        SetupFromRunnerParams(runnerParams, addOnsParams);
    }

    void SetupFromGuiFunction(
        const VoidFunction& guiFunction,
        const std::string& windowTitle,
        bool windowSizeAuto,
        bool windowRestorePreviousGeometry,
        const ScreenSize& windowSize,
        float fpsIdle,

        // AddOnsParams below:
        bool withImplot,
        bool withImplot3d,
        bool withMarkdown,
        bool withNodeEditor,
        bool withTexInspect,
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        const std::optional<NodeEditorConfig>& withNodeEditorConfig,
#endif
        const std::optional<ImGuiMd::MarkdownOptions> & withMarkdownOptions
    )
    {
        HelloImGui::SimpleRunnerParams simpleRunnerParams;
        simpleRunnerParams.guiFunction = guiFunction;
        simpleRunnerParams.windowTitle = windowTitle;
        simpleRunnerParams.windowSizeAuto = windowSizeAuto;
        simpleRunnerParams.windowRestorePreviousGeometry = windowRestorePreviousGeometry;
        simpleRunnerParams.windowSize = windowSize;
        simpleRunnerParams.fpsIdle = fpsIdle;

        AddOnsParams addOnsParams;
        addOnsParams.withImplot = withImplot;
        addOnsParams.withImplot3d = withImplot3d;
        addOnsParams.withMarkdown = true;
        addOnsParams.withNodeEditor = withNodeEditor;
        addOnsParams.withTexInspect = withTexInspect;
#ifdef IMGUI_BUNDLE_WITH_IMGUI_NODE_EDITOR
        addOnsParams.withNodeEditorConfig = withNodeEditorConfig;
#endif
        addOnsParams.withMarkdownOptions = withMarkdownOptions;

        SetupFromSimpleRunnerParams(simpleRunnerParams, addOnsParams);
    }

    void Render()
    {
        HelloImGui::ManualRender::Render();
    }

    void TearDown()
    {
        TrySwitchToNotInitialized();
        HelloImGui::ManualRender::TearDown();
        Priv_TearDown();
    }
} // namespace ManualRender

} // namespace ImmApp
