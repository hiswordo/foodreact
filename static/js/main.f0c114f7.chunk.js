(this.webpackJsonpfoodcard=this.webpackJsonpfoodcard||[]).push([[0],{22:function(e,t,c){},29:function(e,t,c){"use strict";c.r(t);var n=c(0),r=c.n(n),s=c(15),a=c.n(s),o=(c(22),c(1)),j=function(){return Object(o.jsxs)("nav",{className:"navbar",children:[Object(o.jsx)("h1",{children:"Little Food Planet"}),Object(o.jsxs)("div",{className:"link",children:[Object(o.jsx)("a",{href:"./",children:"Home"}),Object(o.jsx)("a",{href:"./create",children:"New"})]})]})},i=c(8),d=function(e){var t=e.cards;return console.log(t),Object(o.jsx)("div",{className:"card-list",children:t.cards.map((function(e){return Object(o.jsxs)("div",{className:"card-preview",children:[Object(o.jsx)("h2",{children:e.title}),Object(o.jsx)("img",{src:e.body,alt:"Cover"}),Object(o.jsx)("p",{children:e.stars})]},e.id)}))})},l=function(e){var t=Object(n.useState)(null),c=Object(i.a)(t,2),r=c[0],s=c[1],a=Object(n.useState)(!0),o=Object(i.a)(a,2),j=o[0],d=o[1],l=Object(n.useState)(null),b=Object(i.a)(l,2),h=b[0],u=b[1];return Object(n.useEffect)((function(){var t=new AbortController;return setTimeout((function(){fetch(e,{signal:t.signal}).then((function(e){if(console.log(e),!e.ok)throw Error("Could not fetch the data for that source!!!!");return e.json()})).then((function(e){d(!1),s(e),u(null)})).catch((function(e){"AbortError"===e.name?console.log("fetch aborted"):(d(!1),u(e.message))}))}),1e3),function(){return t.abort()}}),[e]),{data:r,isPending:j,error:h}},b=function(){var e=l("https://hiswordo.github.io/jsnai/db.json"),t=e.data,c=e.isPending,r=e.error,s=Object(n.useState)(!1),a=Object(i.a)(s,2),j=(a[0],a[1]),b=Object(n.useState)("new guest"),h=Object(i.a)(b,2);h[0],h[1];return Object(n.useEffect)((function(){j(!0)}),[]),Object(o.jsxs)("div",{className:"home",children:[r&&Object(o.jsx)("div",{children:r}),c&&Object(o.jsx)("h2",{children:"Loading ... "}),t&&Object(o.jsx)(d,{cards:t})]})},h=c(10),u=c(2),O=function(){return Object(o.jsxs)("div",{className:"not-found",children:[Object(o.jsx)("h2",{children:"Sorry"}),Object(o.jsx)("p",{children:"Only some tiny rocks here..."}),Object(o.jsx)(h.b,{to:"./",children:"Back to Home, thank you so much~"})]})};var f=function(){return Object(o.jsx)(h.a,{children:Object(o.jsxs)("div",{className:"App",children:[Object(o.jsx)(j,{}),Object(o.jsx)("div",{className:"content",children:Object(o.jsxs)(u.c,{children:[Object(o.jsx)(u.a,{exact:!0,path:"/foodreact/",children:Object(o.jsx)(b,{})}),Object(o.jsx)(u.a,{path:"/foodreact/*",children:Object(o.jsx)(O,{})})]})})]})})};a.a.render(Object(o.jsx)(r.a.StrictMode,{children:Object(o.jsx)(f,{})}),document.getElementById("root"))}},[[29,1,2]]]);
//# sourceMappingURL=main.f0c114f7.chunk.js.map