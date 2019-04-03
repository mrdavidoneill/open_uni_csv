// This has been set up in a language agnostic way, but to add more languages would
// need a way to load an object based on the document.documentElement.lang attribute.
function OULanguageTranslation() {

    this.requiresTranslation = false;

}

OULanguageTranslation.init = function(targetElement) {
    // If we werent passed a specific value to translate, find them all ourself.
    var workItems = (targetElement && targetElement.nodeType) ? targetElement : document.querySelectorAll("[data-translate]");

    // If the document contains a lang we know about then flag that we should do the translation
    if (document.documentElement.lang !== "") {
        this.requiresTranslation = document.documentElement.lang === "cy" ? true : false;

        // TODO: If we ever do more langauges, replace the cymraeg CSS class with cy in the LESS source
        var LanguageClass = "cymraeg"; // = document.body.className;
        if (this.requiresTranslation === true && (' ' + document.body.className + ' ').indexOf(" " + LanguageClass + " ") === -1)  {
            document.body.className += ' ' + LanguageClass; // Apply CSS relevant to this langauge
        }
    }

    if (this.requiresTranslation) {
        // Translate each element targeted with a [data-translate]
        if (workItems.constructor === NodeList) {
            for (var i = 0; i < workItems.length; i++){
                OULanguageTranslation.translate(workItems[i]);
            }
        }
        else {
            OULanguageTranslation.translate(workItems);
        }
    }

};

OULanguageTranslation.translate = function(match) {

    var translateObject = new TranslationArea(match);
    // If we have a match, translate it
    if (translateObject.TranslateText()) {
        translateObject.setText();
    }
};

function TranslationArea(targetElement) {

    this.targetElement = targetElement;
    this.translatedText = "";
    this.warning = false;

    this.getText = function () {
        if (this.targetElement.nodeName === 'INPUT') {
            return this.targetElement.getAttribute("placeholder").trim();
        }
        else {
            return this.targetElement.innerHTML.trim();
        }
    };
    this.originalText = this.getText();

    this.setText = function () {
        if (this.targetElement.nodeName === 'INPUT') {
            this.targetElement.setAttribute("placeholder", this.translatedText);
        }
        else {
            this.targetElement.innerHTML = this.translatedText;
        }
    };

    this.TranslateText = function () {
        var warningMessage = " (missing welsh traslation)";
        this.originalText = this.originalText.replace(warningMessage, "");
        var textKey = this.originalText.replace(/<[^>]+>/g, '').replace("&nbsp;", '').trim();
        this.translatedText = this.originalText.replace(textKey, _translations[textKey]);

        if (textKey in _translations) {
            return true;
        } else {
            if (!isLive()) { // Otherwise flag that we were asked to translate something with no translation (but not on live)
                this.translatedText = this.originalText + warningMessage;
                this.warning = true;
                return true;
            } else {
                this.translatedText = this.originalText;
                return false;
            }
        }
    };
}


if (typeof String.prototype.trim !== 'function') {
    String.prototype.trim = function () {
        if (this !== null) {
            return this.replace(/^\s+|\s+$/g, '');
        }
        return this;
    };
}

// Start translation code after page is loaded
window.addEventListener ? window.addEventListener("load", OULanguageTranslation.init, false) : window.attachEvent && window.attachEvent("onload", OULanguageTranslation.init);


// Welsh Translations follow.
var _translations = {
	"The Open University": "Y Brifysgol Agored",
	'<i class="int-icon int-icon-arrow-circle-down">&nbsp;</i> Skip to content': '<i class="int-icon int-icon-arrow-circle-down">&nbsp;</i> Ymlaen i’r cynnwys',
	'<I class="int-icon int-icon-arrow-circle-down">&nbsp;</I>Skip to content': '<i class="int-icon int-icon-arrow-circle-down">&nbsp;</i> Ymlaen i’r cynnwys', // IE8 markup format
	"Skip to content": "Ymlaen i’r cynnwys",
	"Sign in": "Mewngofnodi",
	"Sign out": "Allgofnodi",
	"My Account": "Fy nghyfrif",
	"StudentHome": "HafanMyfyrwyr",
	"TutorHome": "HafanTiwtoriaid",
	"IntranetHome": "HafanMewnrwyd",
	"Contact the OU": "Cysylltu &acirc;'r OU",
	"Contact us": "Cysylltu &acirc; ni",
	"Accessibility": "Hygyrchedd",
	"Search the OU": "Chwilio’r OU",
	"Jobs": "Swyddi",
	"Conditions of use": "Amodau defnyddio",
	"Privacy and cookies": "Preifatrwydd a chwcis",
	"Modern Slavery Act (pdf 149kb)": "Deddf Gaethwasiaeth Fodern (pdf 149kb)",
	"Copyright": "Hawlfraint",
	"All rights reserved. The Open University is incorporated by Royal Charter (RC 000391), an exempt charity in England &amp; Wales and a charity registered in Scotland (SC 038302). The Open University is authorised and regulated by the Financial Conduct Authority in relation to its secondary activity of credit broking.":
		"Cedwir pob hawl. Mae’r Brifysgol Agored yn gorfforedig drwy Siarter Brenhinol (RC000391), yn elusen a eithrir yng Nghymru a Lloegr ac yn elusen gofrestredig yn yr Alban (SC038302). Awdurdodir a rheoleiddir y Brifysgol Agored gan yr Awdurdod Ymddygiad Ariannol o ran ei weithgarwch eilradd o froceru credyd. ",
	"Cookies on our website": "Cwcis ar ein gwefan",
	"We use cookies to make sure our websites work effectively and to improve your user experience.  If you continue to use this site we will assume that you are happy with this. However, you can change your cookie settings at any time.": "Rydym yn defnyddio cwcis i sicrhau bod ein gwefannau yn gweithio'n effeithiol ac i wella eich profiad fel defnyddiwr. Os byddwch yn parhau i ddefnyddio'r wefan, byddwn yn tybio eich bod yn fodlon gyda hyn. Fodd bynnag, gallwch newid eich gosodiadau cwcis unrhyw dro. ",
	"More Info/Change Settings.": "Mwy o wybodaeth/newid gosodiadau.",
	"Continue": "Parhau"
};