# Command: deepcheck

This command defines the AI-driven process for performing a comprehensive analysis of the directory structure under inbox/ to ensure it is balanced, coherent, and optimally organized.

## Objective

To evaluate the knowledge base's structure for thematic consistency and logical balance, identifying opportunities to improve organization through merging, splitting, or relocating folders and files.

## AI Execution Flow

1.  **Full Knowledge Base Scan**: The AI model will recursively scan all subdirectories within the `index/` directory to build a complete map of all subdirectories and the Markdown files they contain.

2.  **Thematic Analysis of Directories**: For each directory containing Markdown files, the model will perform a semantic analysis to establish its "thematic center."
    *   It will analyze the content of all files within that directory.
    *   It will generate a concise summary of the dominant topic or purpose of the directory (e.g., "This folder contains technical tutorials on Docker and containerization.").

3.  **Structural Health Assessment**: The model will use the thematic centers to perform the following checks:

    *   **Cohesion Check (File-level)**:
        *   **Action**: For each file in a directory, compare its individual topic against the directory's overall thematic center.
        *   **Output**: Flag files that are "thematic outliers" (i.e., they don't belong in that folder).
        *   **Example**: In a `/python/` directory, a file about JavaScript would be flagged. A suggestion would be made to move it to `/javascript/` or a more appropriate location.

    *   **Balance Check (Folder-level)**:
        *   **Identify Overly Broad Folders (Candidates for Splitting)**:
            *   **Condition**: A folder contains a high number of files (e.g., >15) AND the content analysis reveals several distinct, major sub-topics.
            *   **Suggestion**: Propose splitting the folder into more specific subdirectories.
            *   **Example**: A `/programming/` folder with 50 notes might be split into `/python/`, `/go/`, and `/devops/`.

        *   **Identify Overly Specific Folders (Candidates for Merging)**:
            *   **Condition**: Two or more folders have very few files (e.g., <3) AND their thematic centers are highly similar.
            *   **Suggestion**: Propose merging these folders into a single, more comprehensive directory.
            *   **Example**: Folders `/git/` and `/github-actions/` could be merged into a single `/git-and-vcs/` directory.

4.  **Generate Comprehensive Report**: The AI will produce a report detailing its findings and actionable recommendations. The report will be structured for clarity:

    *   **Overall Health Score**: A qualitative score (e.g., Excellent, Good, Needs Improvement) with a brief justification.
    *   **Files to Move**: A list of thematic outliers and their suggested new locations.
    *   **Folders to Split**: A list of large, overly broad folders with proposals for the new, more focused subdirectories.
    *   **Folders to Merge**: A list of small, related folders with proposals for a unified new directory.

5.  **User Confirmation**: The report and its suggested actions will be presented to the user. The AI will not perform any restructuring until the user reviews and approves the plan.

6.  **Commit and Push**: After the user confirms the changes, the AI will stage all changes, commit them with a descriptive message, and push them to the remote repository.
