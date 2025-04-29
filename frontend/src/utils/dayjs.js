import dayjs from "dayjs"
import updateLocale from "dayjs/plugin/updateLocale"
import localizedFormat from "dayjs/plugin/localizedFormat"
import relativeTime from "dayjs/plugin/relativeTime"
import isToday from "dayjs/plugin/isToday"
import isYesterday from "dayjs/plugin/isYesterday"
import isBetween from "dayjs/plugin/isBetween"

// Import required locales here
// TODO: This is a temporary solution. Ideally, locales should be loaded dynamically 
// based on the user's language setting, potentially integrated with translationsPlugin.js
import 'dayjs/locale/ru';

dayjs.extend(updateLocale)
dayjs.extend(localizedFormat)
dayjs.extend(relativeTime)
dayjs.extend(isToday)
dayjs.extend(isYesterday)
dayjs.extend(isBetween)

// Update Russian locale month names to be capitalized
dayjs.updateLocale('ru', {
  months: [
    "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
    "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
  ]
});

export default dayjs
