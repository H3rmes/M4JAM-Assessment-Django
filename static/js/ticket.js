/**
 * @author Bongani Ndhlovu
 * @description Tinymce setup
 */
$(function() {
    tinymce.init({
        // selector: "#description", tinyMCE hides text-arae : Bug
        theme: "modern",
        mobile: {
            theme: "mobile",
            plugins: ['autosave']
        },
        plugins: 'spellchecker',
        browswer_spellcheck: true
    });
}); 