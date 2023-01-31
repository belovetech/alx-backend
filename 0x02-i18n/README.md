# i18n

Pybabel Commands:

```babel
Innitialize translations
    - pybabel extract -F babel.cfg -o messages.pot .

Generate two dictionaries
    - pybabel init -i messages.pot -d translations -l en
    - pybabel init -i messages.pot -d translations -l fr

Compile the dictionaries:
    - pybabel compile -d translations
```
