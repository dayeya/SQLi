from app.website import create_app


def main() -> None:
    app = create_app()
    app.run(host='127.0.0.1', port=50000, debug=True)


if __name__ == '__main__':
    main()
