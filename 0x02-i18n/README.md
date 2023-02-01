# i18n -> Internalization

Internationalization (sometimes shortened to "I18N , meaning "I - eighteen letters -N") is the process of planning and implementing products and services so that they can easily be adapted to specific local languages and cultures, a process called localization .

## flask-babel

flask-babel is a Flask extension that makes working with translations very easy

## pytz

This library allows accurate and cross platform timezone calculations.

#### Pybabel Commands:

```babel
Innitialize translations
    - pybabel extract -F babel.cfg -o messages.pot .

Generate two dictionaries
    - pybabel init -i messages.pot -d translations -l en
    - pybabel init -i messages.pot -d translations -l fr

Compile the dictionaries:
    - pybabel compile -d translations
```
