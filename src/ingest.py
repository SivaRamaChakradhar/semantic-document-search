from pathlib import Path
from typing import List, Dict


def ingest_documents(directory_path: str) -> List[Dict[str, str]]:
    """
    Read all .txt documents from the specified directory.

    Returns:
        List of dictionaries containing:
        - id: filename
        - content: full document text
    """

    directory = Path(directory_path)

    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory_path}")

    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory_path}")

    documents = []

    # Recursive traversal
    for file_path in sorted(directory.rglob("*.txt")):

        try:
            content = file_path.read_text(
                encoding="utf-8",
                errors="replace"
            )

            # Ignore completely empty documents
            if not content.strip():
                print(f"Warning: Skipping empty file: {file_path}")
                continue

            documents.append({
                "id": str(file_path.relative_to(directory)),
                "content": content
            })

        except OSError as exc:
            print(f"Warning: Could not read {file_path}: {exc}")

    return documents