import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from "i18next-browser-languagedetector";
import format from "./i18n-format.js";
import translationEN from "../public/locales/en/translation.json";
import translationES from "../public/locales/es/translation.json";
import translationRO from "../public/locales/ro/translation.json";

const resources = {
  en: {
    translation: translationEN,
  },
  es: {
    translation: translationES,
  },
  ro: {
    translation: translationRO,
  },
};
i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources,
    react: {
      useSuspense: false,
    },
    fallbackLng: "ro",
    interpolation: {
      format,
    },
    whitelist: ["es", "en", "ro"],
  });
