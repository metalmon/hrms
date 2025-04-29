import dayjs from "@/utils/dayjs"; // Import dayjs

function makeTranslationFunction() {
	let messages = {};
	return {
		translate,
		load: () => Promise.allSettled([
			setup(),
			// TODO: load dayjs locales
			setDayjsLocaleBasedOnSystem(),
		]),
	}

	async function setup() {
		if (window.frappe?.boot?.__messages) {
			messages = window.frappe?.boot?.__messages;
			// Set dayjs locale even if using cached messages
			setDayjsLocaleBasedOnSystem();
			return;
		}

		const lang = window.frappe?.boot?.lang ?? navigator.language;
		const url = new URL("/api/method/frappe.translate.load_all_translations", location.origin);
		url.searchParams.append("lang", lang);
		url.searchParams.append("hash", window.frappe?.boot?.translations_hash || window._version_number || Math.random()); // for cache busting
		// url.searchParams.append("app", "hrms");

		try {
			const response = await fetch(url);
			messages = await response.json() || {}
			// Set dayjs locale after fetching messages
			setDayjsLocaleBasedOnSystem();
		} catch (error) {
			console.error("Failed to fetch translations:", error)
			// Attempt to set dayjs locale even on error using fallback
			setDayjsLocaleBasedOnSystem();
		}
	}

	// Function to set dayjs locale based on Frappe/browser settings
	function setDayjsLocaleBasedOnSystem() {
		try {
			const lang = window.frappe?.boot?.lang || navigator.language || 'en';
			const baseLocale = lang.split('-')[0].toLowerCase();
			dayjs.locale(baseLocale);
			// console.log(`Dayjs locale set to: ${baseLocale}`);
		} catch (e) {
			console.warn(`Failed to set dayjs locale based on system settings. Falling back to 'en'. Error: ${e}`);
			dayjs.locale('en'); // Fallback to English
		}
	}

	function translate(txt, replace, context = null) {
		if (!txt || typeof txt != "string") return txt;

		let translated_text = "";
		let key = txt;
		if (context) {
			translated_text = messages[`${key}:${context}`];
		}
		if (!translated_text) {
			translated_text = messages[key] || txt;
		}
		if (replace && typeof replace === "object") {
			translated_text = format(translated_text, replace);
		}

		return translated_text;
	}

	function format(str, args) {
		if (str == undefined) return str;

		let unkeyed_index = 0;
		return str.replace(
			/\{(\w*)\}/g,
			(match, key) => {
				if (key === "") {
					key = unkeyed_index;
					unkeyed_index++;
				}
				if (key == +key) {
					return args[key] !== undefined ? args[key] : match;
				}
			}
		);
	}
}

const { translate, load } = makeTranslationFunction();

export const translationsPlugin = {
	async isReady() {
		await load();
	},
	install(/** @type {import('vue').App} */ app, options) {
		const __ = translate;
		// app.mixin({ methods: { __ } })
		app.config.globalProperties.__ = __;
		app.provide("$translate", __);
	},
}
