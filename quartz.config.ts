import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4.0 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Alex Racapé",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "alexracape.github.io",
    ignorePatterns: ["private", "_templates", ".obsidian"],
    defaultDateType: "created",
    theme: {
      typography: {
        header: "Kumbh Sans",
        body: "Roboto",
        code: "Fira Code",
      },
      colors: {
        lightMode: {
          light: "#faf8f0",
          lightgray: "#f0ede0",
          gray: "#d63638",
          darkgray: "#2b2b2b",
          dark: "#1a1a1a",
          secondary: "#1e5aff",
          tertiary: "#ffc400",
          highlight: "rgba(255, 196, 0, 0.18)",
          textHighlight: "rgba(255, 196, 0, 0.35)",
        },
        darkMode: {
          light: "#0d0d0a",
          lightgray: "#1c1c18",
          gray: "#e85d5d",
          darkgray: "#e8e6d8",
          dark: "#faf8f0",
          secondary: "#3d70ff",
          tertiary: "#ffd23d",
          highlight: "rgba(255, 210, 61, 0.15)",
          textHighlight: "rgba(255, 210, 61, 0.25)",
        },
      },
      cdnCaching: true,
      fontOrigin: "googleFonts",
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        // you can add 'git' here for last modified from Git
        // if you do rely on git for dates, ensure defaultDateType is 'modified'
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.HomePage(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
