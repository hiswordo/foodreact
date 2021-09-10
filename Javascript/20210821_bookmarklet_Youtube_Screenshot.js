

/* javascript: (function () {
    var canvas = document.createElement('canvas');
    canvas.width = 640;
    canvas.height = 480;
    var ctx = canvas.getContext('2d');
    var video = document.querySelector(".html5-video-container > video");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    var dataURI = canvas.toDataURL('image/jpeg');
    console.log(dataURI);
})();
 */
// @link [GitHub - ReeganExE/youtube-screenshot: Take Screenshot of Youtube video or video on any sites](https://github.com/ReeganExE/youtube-screenshot#floppy_disk-screengrab) at 2021/8/21

//----ScreenShot----
'use strict';

(function(window, document) {
    var canvas = document.createElement('canvas');
    var video = document.querySelector('video');
    var ctx = canvas.getContext('2d');

    // Change the size here
    canvas.width = parseInt(video.offsetWidth);
    canvas.height = parseInt(video.offsetHeight);
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Won't work on file:/// URLs. SecurityError: Tainted canvases may not be exported.
    var base64ImageData = canvas.toDataURL('image/jpeg');
    var filename = 'snap-' + canvas.width + 'x' + canvas.height + '-' + video.currentTime + '.jpg';

    // Wrap <img> in link to download image because 
    // the context menu Save Image as... is blocked for security reasons
    var a = document.createElement('a');
    a.download = filename;
    a.href = base64ImageData;

    var img = document.createElement('img');
    img.src = base64ImageData;
    img.alt = filename;
    img.title = 'Click to save ' + filename;

    window.open().document.body.appendChild(a).appendChild(img);
})(window, document);

// in short: javascript:"use strict";!function(window,document){var canvas=document.createElement("canvas"),video=document.querySelector("video"),ctx=canvas.getContext("2d");canvas.width=parseInt(video.offsetWidth),canvas.height=parseInt(video.offsetHeight),ctx.drawImage(video,0,0,canvas.width,canvas.height);var base64ImageData=canvas.toDataURL("image/jpeg"),filename="snap-"+canvas.width+"x"+canvas.height+"-"+video.currentTime+".jpg",a=document.createElement("a");a.download=filename,a.href=base64ImageData;var img=document.createElement("img");img.src=base64ImageData,img.alt=filename,img.title="Click to save "+filename,window.open().document.body.appendChild(a).appendChild(img)}(window,document);

//----Screen Grab----
'use strict';

(function (window, document) {
    var canvas = document.createElement('canvas');
    var video = document.querySelector('video');
    var ctx = canvas.getContext('2d');

    // Change the size here
    canvas.width = parseInt(video.offsetWidth);
    canvas.height =  parseInt(video.offsetHeight);
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    var a = document.createElement('a');
    a.download = 'snap-' + canvas.width + 'x' + canvas.height + '-' + video.currentTime + '.jpg';
    // Won't work on file:/// URLs. SecurityError: Tainted canvases may not be exported.
    a.href = canvas.toDataURL('image/jpeg');
    document.body.appendChild(a).click();
    a.remove();
})(window, document)

// in short: javascript:"use strict";!function(window,document){var canvas=document.createElement("canvas"),video=document.querySelector("video"),ctx=canvas.getContext("2d");canvas.width=parseInt(video.offsetWidth),canvas.height=parseInt(video.offsetHeight),ctx.drawImage(video,0,0,canvas.width,canvas.height);var a=document.createElement("a");a.download="snap-"+canvas.width+"x"+canvas.height+"-"+video.currentTime+".jpg",a.href=canvas.toDataURL("image/jpeg"),document.body.appendChild(a).click(),a.remove()}(window,document);

//----Screen Grab v2----
'use strict';

(function (window, document) {
    var canvas = document.createElement('canvas');
    var video = document.querySelector('.captions-text')
    var ctx = canvas.getContext('2d');

    // Change the size here
    canvas.width = parseInt(video.offsetWidth);
    ctx.drawImage(video, 0, 0, canvas.width, 100);
    
    var a = document.createElement('a');
    a.download = 'snap-' + canvas.width + 'x' + canvas.height + '-' + video.currentTime + '.png';
    // Won't work on file:/// URLs. SecurityError: Tainted canvases may not be exported.
    // a.href = canvas.toDataURL('image/png');
    document.body.appendChild(a).click();
    a.remove();
})(window, document)