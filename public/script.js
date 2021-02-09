// const flask = new CodeFlask('#input', { language: 'js',
// defaultTheme: true
// });
// let output = document.getElementById('output')
// let Submit = document.getElementById('submit')

// // How to listen for changes on your editor
// flask.onUpdate((code) => {
//   //...
// });

// // How to update your editor with custom content:
// const new_content = 'console.log("test")';
// flask.updateCode(new_content);

// // Submit.onClick = submit();

// function submit() {
// 	output.innerText = 'test' + encodeURI(flask.code)
// };

// var clipboard = new ClipboardJS('#copy');

// clipboard.on('success', function(e) {
//   e.clearSelection();
// 	M.toast({html: 'Succesfully copied to clipboard!', classes: 'rounded'})
// });

// clipboard.on('error', function(e) {
//   e.clearSelection();
// 	M.toast({html: 'Hmmm. Something went wrong.', classes: 'rounded'})
// });