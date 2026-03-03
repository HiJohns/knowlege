# Command: rootclean

This command defines the AI-driven process for organizing all Markdown files currently in the root directory into the most appropriate subdirectories.

## Objective

To analyze the content of each Markdown file in the `inbox/` directory of the knowledge base, determine its primary topic, and recommend moving it to the most suitable existing or new subdirectory.

## AI Execution Flow

1.  **Identify Target Files**: The AI model will begin by listing all `*.md` files located in the project's `index/` directory.

2.  **Content Analysis per File**: For each file identified, the model will perform the following steps:
    *   **Read Content**: Ingest the full content of the Markdown file, including the YAML frontmatter.
    *   **Semantic Understanding**: Analyze the text to determine its core subject matter, key concepts, and overall theme. The `title` and `tags` from the frontmatter will serve as strong initial hints, but the main body text is the primary source of truth.
    *   **Topic Extraction**: Synthesize the analysis into a concise topic name (e.g., "Venture Capital," "Python Programming," "Market Analysis").

3.  **Directory Analysis**: The AI model will list all existing subdirectories within the knowledge base to understand the current organizational structure.

4.  **Matching and Suggestion**: For each file, the model will decide on the best placement:
    *   **Match Existing**: It will compare the file's extracted topic with the themes of the existing directories. A directory's theme is determined by the collective topics of the files it already contains.
    *   **Propose New**: If no existing directory is a strong semantic match, the model will propose creating a new directory. The proposed name will be a sanitized, URL-friendly version of the extracted topic (e.g., "venture-capital").

5.  **Generate Report**: The model will compile a list of suggested actions. Each suggestion will be clear and require user confirmation.

    *   **Example Suggestion 1 (Move to existing):**
        > - **File**: `2026-03-03-clip-logic-behind-foreign-capital-and-a-shares.md`
        > - **Topic**: Analysis of foreign capital flows in the Chinese stock market.
        > - **Recommendation**: Move to subdirectory `finance/`.
        > - **Command**: `mv 2026-03-03-clip-logic-behind-foreign-capital-and-a-shares.md finance/`

    *   **Example Suggestion 2 (Create new and move):**
        > - **File**: `my-notes-on-large-language-models.md`
        > - **Topic**: A collection of thoughts on LLM architecture.
        > - **Recommendation**: Create new subdirectory `large-language-models/` and move the file there.
        > - **Command**: `mkdir -p large-language-models && mv my-notes-on-large-language-models.md large-language-models/`

6.  **User Confirmation**: The final list of commands will be presented to the user. The AI will await approval before executing any file system modifications.
