CKEDITOR.addCss('.cke_editable { font-size: 15px; padding: 2em; }');

CKEDITOR.replace('editor1', {
    toolbar: [{
        name: 'document',
        items: ['Print']
    },
        {
            name: 'clipboard',
            items: ['Undo', 'Redo']
        },
        {
            name: 'styles',
            items: ['Format', 'Font', 'FontSize']
        },
        {
            name: 'colors',
            items: ['TextColor', 'BGColor']
        },
        {
            name: 'align',
            items: ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']
        },
        '/',
        {
            name: 'basicstyles',
            items: ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat', 'CopyFormatting']
        },
        {
            name: 'links',
            items: ['Link', 'Unlink']
        },
        {
            name: 'paragraph',
            items: ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']
        },
        {
            name: 'insert',
            items: ['Image', 'Table']
        },
        {
            name: 'tools',
            items: ['Maximize']
        },
        {
            name: 'editing',
            items: ['Scayt']
        }
    ],

    extraAllowedContent: 'h3{clear};h2{line-height};h2 h3{margin-left,margin-top}',

    // Adding drag and drop image upload.
    extraPlugins: 'print,format,font,colorbutton,justify,uploadimage',
    uploadUrl: '/apps/ckfinder/3.4.5/core/connector/php/connector.php?command=QuickUpload&type=Files&responseType=json',

    // Configure your file manager integration. This example uses CKFinder 3 for PHP.
    filebrowserBrowseUrl: '/apps/ckfinder/3.4.5/ckfinder.html',
    filebrowserImageBrowseUrl: '/apps/ckfinder/3.4.5/ckfinder.html?type=Images',
    filebrowserUploadUrl: '/apps/ckfinder/3.4.5/core/connector/php/connector.php?command=QuickUpload&type=Files',
    filebrowserImageUploadUrl: '/apps/ckfinder/3.4.5/core/connector/php/connector.php?command=QuickUpload&type=Images',

    height: 560,

    removeDialogTabs: 'image:advanced;link:advanced',
    removeButtons: 'PasteFromWord'
});