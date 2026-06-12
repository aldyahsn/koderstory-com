module.exports = {
  content: [
    "./templates/**/*.html",
    "./core/**/*.py",
    "./pages/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        brand: "var(--color-primary)",
        ink: "var(--color-text)",
        canvas: "var(--color-background)",
      },
      fontFamily: {
        heading: "var(--font-heading)",
        body: "var(--font-body)",
      },
      borderRadius: {
        token: "var(--radius-card)",
        button: "var(--radius-button)",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
