(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[500],{2626:(e,t,a)=>{(window.__NEXT_P=window.__NEXT_P||[]).push(["/animeflv",function(){return a(8708)}])},8708:(e,t,a)=>{"use strict";a.r(t),a.d(t,{Button_6e73b3481d4ce4e8c3291302251d189d:()=>H,Fragment_320576ce7b5fe60296d76c9cd0088977:()=>I,Fragment_464511274b8c54989380dff52569332e:()=>R,Root_0d880de1f89674c0d1f67b1b91841539:()=>z,Select__root_69746262c66e63f5c8b30e6d1070912c:()=>B,Table__body_84cfb233fbea2a989d52e66b451d64d6:()=>L,Text_8a7799106269bd6a9757de95b8c9b528:()=>j,Text_e916242bf6a466fd5084211d331507cf:()=>A,Textfield__root_b92c421cd427710579f265a5fb202f46:()=>T,default:()=>O});var n=a(2445),r=a(6540),o=a(2996),s=a(6640),i=a(6142),_=a(9057),c=a(6726),l=a(1795),d=a(2278),h=a(983),g=a(8156),p=a(5765),m=a(922),u=a(8133),f=a.n(u),F=a(1106),x=a.n(F),b=a(5236),v=a(1789),Y=a(9737),C=a(4668),k=a(1637),w=a(6145),E=a(2930),D=a(391),S=a(9188),y=a(3368),N=a.n(y);function A(){let e=(0,r.useContext)(S.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state);return(0,n.FD)(o.E,{as:"p",css:{color:"#FFD700"},children:[e.name+" anime list ",(()=>{switch(JSON.stringify(e.anime_type)){case JSON.stringify("favoritos"):return"Favorites";case JSON.stringify("siguiendo"):return"Following";case JSON.stringify("lista_espera"):return"Watchlist";default:return"Unknown"}})()]})}function I(){let e=(0,r.useContext)(S.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state);return(0,n.Y)(r.Fragment,{children:e.loading?(0,n.Y)(r.Fragment,{children:(0,n.Y)(s.y,{})}):(0,n.Y)(r.Fragment,{children:(0,n.Y)(o.E,{as:"p",children:""})})})}function T(){let[e,t]=(0,r.useContext)(S.EventLoopContext),a=(0,r.useCallback)(t=>e([(0,E.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.set_name",{name:t.target.value},{})],[t],{}),[e,E.Event]);return(0,n.Y)(i.Root,{css:{width:"100%",color:"#FFE08A"},minLength:1,onChange:a,placeholder:"User name",required:!0,size:"2"})}function z(){let[e,t]=(0,r.useContext)(S.EventLoopContext),a=(0,r.useCallback)(t=>{let a=t.target;t.preventDefault(),Object.fromEntries(new FormData(a).entries()),function(){for(var t=arguments.length,a=Array(t),n=0;n<t;n++)a[n]=arguments[n];e([(0,E.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.get_animes",{},{})],a,{})}(t)});return(0,n.Y)(D.bL,{className:"Root ",css:{width:"100%",enterKeySubmit:!0},onSubmit:a,children:(0,n.FD)(_.s,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,n.Y)(T,{}),(0,n.Y)(B,{}),(0,n.Y)(H,{}),(0,n.Y)(I,{})]})})}function R(){let e=(0,r.useContext)(S.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state),[t,a]=(0,r.useContext)(S.EventLoopContext);return(0,n.Y)(r.Fragment,{children:e.has_animes?(0,n.Y)(r.Fragment,{children:(0,n.FD)(_.s,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,n.Y)(c.$,{css:{width:"30%",height:"100%",padding:"0.5em",borderRadius:"1em",color:"#FFD700",backgroundColor:"#5E0303",whiteSpace:"nowrap",justifyContent:"start",alignItems:"center","&:hover":{backgroundColor:"#FF4500"},marginTop:"10px"},onClick:function(){for(var e=arguments.length,a=Array(e),n=0;n<e;n++)a[n]=arguments[n];return t([(0,E.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.copy_data_table",{},{})],a,{})},children:"Copy"}),(0,n.Y)(c.$,{css:{width:"65%",height:"100%",padding:"0.5em",borderRadius:"1em",color:"#FFD700",backgroundColor:"#5E0303",whiteSpace:"nowrap",justifyContent:"start",alignItems:"center","&:hover":{backgroundColor:"#FF4500"},marginTop:"10px"},onClick:function(){for(var e=arguments.length,a=Array(e),n=0;n<e;n++)a[n]=arguments[n];return t([(0,E.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.download_csv_data",{},{})],a,{})},children:"Download CSV"})]})}):(0,n.Y)(r.Fragment,{children:(0,n.Y)(o.E,{as:"p",css:{color:"#FFE08A"},children:"Load animes first to download"})})})}function H(){let e=(0,r.useContext)(S.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state),[t,a]=(0,r.useContext)(S.EventLoopContext),o=(0,r.useCallback)(function(){for(var e=arguments.length,a=Array(e),n=0;n<e;n++)a[n]=arguments[n];return t([(0,E.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.get_animes",{},{})],a,{})},[t,E.Event]);return(0,n.Y)(c.$,{css:{width:"13%",height:"100%",padding:"0.5em",borderRadius:"1em",color:"#FFD700",backgroundColor:"#5E0303",whiteSpace:"nowrap",justifyContent:"start",alignItems:"center","&:hover":{backgroundColor:"#FF4500"}},disabled:""===e.name,onClick:o,children:"Search"})}function B(){let[e,t]=(0,r.useContext)(S.EventLoopContext),a=(0,r.useCallback)(t=>e([(0,E.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.set_anime_type",{anime_type:t},{})],[t],{}),[e,E.Event]);return(0,n.FD)(l.Root,{defaultValue:"favoritos",name:"anime_type",onValueChange:a,required:!0,size:"2",children:[(0,n.Y)(l.Trigger,{css:{name:"anime_type",backgroundColor:"#5E0303",color:"#FFD700"},variant:"soft"}),(0,n.Y)(l.Content,{color:"yellow",css:{color:"#FFE08A"},variant:"soft",children:(0,n.FD)(l.Group,{children:[(0,n.Y)(l.Item,{value:"favoritos",children:"Favorites"}),(0,n.Y)(l.Item,{value:"siguiendo",children:"Following"}),(0,n.Y)(l.Item,{value:"lista_espera",children:"Watchlist"})]})})]})}function L(){let e=(0,r.useContext)(S.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state);return(0,n.Y)(d.Body,{children:(0,n.Y)(n.FK,{children:e.animes.map((e,t)=>(0,n.Y)(d.Row,{children:(0,n.Y)(d.Cell,{css:{whiteSpace:"nowrap",textWrap:"nowrap",color:"#FFE08A"},children:e.title})},t))})})}function j(){let e=(0,r.useContext)(S.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state);return(0,n.Y)(o.E,{as:"p",css:{color:"#FFD700"},children:"Total: "+e.count_animes})}function O(){return(0,n.FD)(r.Fragment,{children:[(0,n.FD)(h.a,{children:[(0,n.Y)(r.Fragment,{children:(0,n.Y)(f(),{strategy:"afterInteractive",children:"document.dispatchEvent.lang='en'"})}),(0,n.Y)(_.s,{align:"start",className:"rx-Stack",css:{position:"sticky",background:"#5E0303",paddingInlineStart:"2em",paddingInlineEnd:"2em",paddingTop:"1em",paddingBottom:"1em",zIndex:"999",top:"0"},direction:"row",gap:"3",children:(0,n.Y)(g.N,{asChild:!0,css:{color:"#FFE08A",textDecoration:"none","&:hover":{color:"var(--accent-8)"}},children:(0,n.Y)(x(),{href:"/",passHref:!0,children:(0,n.Y)(o.E,{as:"p",css:{fontFamily:"Great Vibes","--default-font-family":"Great Vibes",fontWeight:"700",fontSize:"1.5em",color:"#FFD700"},children:"SBH"})})})}),(0,n.Y)(_.s,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,n.FD)(_.s,{align:"start",className:"rx-Stack",css:{maxWidth:"560px",width:"100%",marginTop:"1em",marginBottom:"1em",padding:"2em"},direction:"column",gap:"3",children:[(0,n.FD)(_.s,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,n.FD)(_.s,{align:"start",className:"rx-Stack",direction:"row",gap:"3",children:[(0,n.Y)(p.e,{"aria-label":"icono de perfil",fallback:"SBH",size:"7",src:"/llamas.png"}),(0,n.FD)(_.s,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,n.Y)(m.D,{css:{fontFamily:"Poppins","--default-font-family":"Poppins",fontWeight:"700",color:"#FFD700"},size:"6",children:"Santiago Bauz\xe1 Hirschler"}),(0,n.FD)(_.s,{align:"start",className:"rx-Stack",css:{paddingTop:"1em"},direction:"row",gap:"3",children:[(0,n.Y)(g.N,{"aria-label":"linkedin",asChild:!0,css:{color:"#FFE08A",textDecoration:"none","&:hover":{color:"var(--accent-8)"}},target:"_blank",children:(0,n.Y)(x(),{href:"https://www.linkedin.com/in/santiagobauz%C3%A1-sistemasinformaticos/",passHref:!0,children:(0,n.Y)(b.A,{css:{"&:hover":{color:"#FFD700"},color:"var(--current-color)"}})})}),(0,n.Y)(g.N,{"aria-label":"github",asChild:!0,css:{color:"#FFE08A",textDecoration:"none","&:hover":{color:"var(--accent-8)"}},target:"_blank",children:(0,n.Y)(x(),{href:"https://github.com/s-bauza",passHref:!0,children:(0,n.Y)(v.A,{css:{"&:hover":{color:"#FFD700"},color:"var(--current-color)"}})})}),(0,n.Y)(g.N,{"aria-label":"youtube",asChild:!0,css:{color:"#FFE08A",textDecoration:"none","&:hover":{color:"var(--accent-8)"}},target:"_blank",children:(0,n.Y)(x(),{href:"https://www.youtube.com/@cordico9070/featured",passHref:!0,children:(0,n.Y)(Y.A,{css:{"&:hover":{color:"#FFD700"},color:"var(--current-color)"}})})}),(0,n.Y)(g.N,{"aria-label":"x",asChild:!0,css:{color:"#FFE08A",textDecoration:"none","&:hover":{color:"var(--accent-8)"}},target:"_blank",children:(0,n.Y)(x(),{href:"https://x.com/Cordic0",passHref:!0,children:(0,n.Y)(C.A,{css:{"&:hover":{color:"#FFD700"},color:"var(--current-color)"}})})}),(0,n.FD)(h.a,{css:{position:"relative"},children:[(0,n.Y)(g.N,{"aria-label":"twitch",asChild:!0,css:{color:"#FFE08A",textDecoration:"none","&:hover":{color:"var(--accent-8)"}},target:"_blank",children:(0,n.Y)(x(),{href:"https://www.twitch.tv/cordico",passHref:!0,children:(0,n.Y)(k.A,{css:{"&:hover":{color:"#FFD700"},color:"var(--current-color)"}})})}),(0,n.Y)(w.Q,{})]})]})]})]}),(0,n.Y)(r.Fragment,{children:(0,n.Y)(r.Fragment,{})})]}),(0,n.FD)(_.s,{align:"start",className:"rx-Stack",css:{width:"100%",marginTop:"20px"},direction:"column",gap:"3",children:[(0,n.Y)(m.D,{css:{fontFamily:"Poppins","--default-font-family":"Poppins",fontWeight:"700",color:"#FFD700"},children:"Animelfv Info"}),(0,n.Y)(z,{}),(0,n.Y)(_.s,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"3",children:(0,n.FD)(h.a,{css:{width:"100%",height:"400px",marginTop:"20px"},children:[(0,n.FD)(_.s,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"row",gap:"3",children:[(0,n.Y)(A,{}),(0,n.Y)(h.a,{css:{textAlign:"right",flex:"1"},children:(0,n.Y)(j,{})})]}),(0,n.Y)(d.Root,{css:{width:"100%",height:"calc(100% - 40px)"},children:(0,n.Y)(L,{})}),(0,n.Y)(_.s,{align:"start",className:"rx-Stack",css:{width:"100%"},direction:"row",justify:"end",gap:"3",children:(0,n.Y)(R,{})})]})})]})]})}),(0,n.FD)(_.s,{align:"start",className:"rx-Stack",css:{paddingTop:"0.5em",paddingBottom:"2em",paddingInlineStart:"2em",paddingInlineEnd:"2em",alignItems:"center",color:"#FFE08A"},direction:"column",gap:"3",children:[(0,n.Y)("img",{alt:"Campana de fuego",src:"/campana.jpg"}),(0,n.FD)(_.s,{align:"start",className:"rx-Stack",css:{alignItems:"center"},direction:"column",justify:"center",gap:"0",children:[(0,n.Y)(o.E,{as:"p",css:{fontSize:"0.8em"},children:"\xa9 2025 Santiago Bauz\xe1 Hirschler"}),(0,n.Y)(o.E,{as:"p",css:{fontSize:"0.8em"},children:"Nobody has greater satisfaction than overcoming themselves."})]})]})]}),(0,n.FD)(N(),{children:[(0,n.Y)("title",{children:"Animeflv Info"}),(0,n.Y)("meta",{content:"Animeflv Info DESCRIPTION",name:"description"}),(0,n.Y)("meta",{content:"/favicon-16x16.png",property:"og:image"}),(0,n.Y)("meta",{name:"og:preview_image"})]})]})}},6145:(e,t,a)=>{"use strict";a.d(t,{Q:()=>_});var n=a(2445),r=a(6540),o=a(983),s=a(9188),i=a(2930);function _(){(0,r.useEffect)(()=>(!function(){for(var e=arguments.length,a=Array(e),n=0;n<e;n++)a[n]=arguments[n];t([(0,i.Event)("reflex___state____state.link_bio___state___page_state____pasge_state.twitch_live",{},{})],a,{})}(),()=>{}),[]);let e=(0,r.useContext)(s.StateContexts.reflex___state____state__link_bio___state___page_state____pasge_state),[t,a]=(0,r.useContext)(s.EventLoopContext);return(0,n.Y)(o.a,{className:e.live_status.live?"blink":"",css:{width:"0.5em",height:"0.5em",backgroundColor:e.live_status.live?"green":"red",borderRadius:"50%",position:"absolute",top:"65%",left:"20px"}})}}},e=>{var t=t=>e(e.s=t);e.O(0,[236,636,593,792],()=>t(2626)),_N_E=e.O()}]);