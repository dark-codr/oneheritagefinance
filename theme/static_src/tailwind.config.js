/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    darkMode : 'media',
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../../oneheritagefinance/templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../oneheritagefinance/templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            screens: {
              xs: '475px',
              ...defaultTheme.screens
            },
            fontFamily: {
              "raleway": ["'Raleway'", "Be Vietnam Pro", "sans-serif"],
              "cursive": ["'Poiret One'", "cursive"],
            },
            colors: {
              "body": "#EBE6E9",
              grey : {
                900: "#22201f",
                800: "#323230",
                700: "#393C49",
                400: "#b4b7c0",
                100: "#EBE6E9"
              },
              lemon: {
                400: "#edec8e",
                700: "#e7e74f",
                900: "#b1bf3d"
              },
              primary: "#e7e74f",
              "light": "#b4b7c0",
              "dark": "#22201f"
            },
            boxShadow : {
              primary : "6px 6px 10px rgba(177,191,61, 0.7)",
            }
        },
    },
    variants: {
        extend: {},
        scrollBar: ["rounded"],
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require('tailwind-scrollbar-hide'),
        require('tailwind-scrollbar')
    ],
}
