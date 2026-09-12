import argparse
import json
from pathlib import Path

from src.indexer import build_index
from src.search import SemanticSearcher


def positive_integer(value):

    number = int(value)

    if number <= 0:
        raise argparse.ArgumentTypeError(
            "k must be a positive integer"
        )

    return number


def main():

    parser = argparse.ArgumentParser(
        description="Semantic Document Search Engine"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # --------------------------------
    # INDEX COMMAND
    # --------------------------------

    index_parser = subparsers.add_parser(
        "index",
        help="Build the document search index"
    )

    index_parser.add_argument(
        "--data-dir",
        required=True,
        help="Directory containing .txt documents"
    )

    index_parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory where index will be saved"
    )

    # --------------------------------
    # SEARCH COMMAND
    # --------------------------------

    search_parser = subparsers.add_parser(
        "search",
        help="Search indexed documents"
    )

    search_parser.add_argument(
        "--index-dir",
        required=True,
        help="Directory containing the index"
    )

    query_group = search_parser.add_mutually_exclusive_group(
        required=True
    )

    query_group.add_argument(
        "--query",
        type=str,
        help="Single search query"
    )

    query_group.add_argument(
        "--batch-file",
        type=str,
        help="File containing one query per line"
    )

    search_parser.add_argument(
        "--k",
        type=positive_integer,
        default=5,
        help="Number of results to return"
    )

    args = parser.parse_args()

    # --------------------------------
    # ROUTING
    # --------------------------------

    if args.command == "index":

        build_index(
            args.data_dir,
            args.output_dir
        )

    elif args.command == "search":

        searcher = SemanticSearcher(
            args.index_dir
        )

        # Single query
        if args.query:

            results = searcher.search(
                args.query,
                args.k
            )

            print(
                json.dumps(
                    {
                        "query": args.query,
                        "results": results
                    },
                    indent=2,
                    ensure_ascii=False
                )
            )

        # Batch queries
        elif args.batch_file:

            batch_path = Path(args.batch_file)

            if not batch_path.exists():
                raise FileNotFoundError(
                    f"Batch file not found: {batch_path}"
                )

            queries = batch_path.read_text(
                encoding="utf-8"
            ).splitlines()

            for query in queries:

                query = query.strip()

                if not query:
                    continue

                results = searcher.search(
                    query,
                    args.k
                )

                print("\n" + "=" * 70)
                print(f"QUERY: {query}")
                print("=" * 70)

                print(
                    json.dumps(
                        results,
                        indent=2,
                        ensure_ascii=False
                    )
                )


if __name__ == "__main__":
    main()