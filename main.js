"use strict";
const toggle=document.querySelector("#menu-toggle");
const nav=document.querySelector("#navlinks");
toggle?.addEventListener("click",()=>{const expanded=toggle.getAttribute("aria-expanded")==="true";toggle.setAttribute("aria-expanded",String(!expanded));toggle.setAttribute("aria-label",expanded?"Ouvrir le menu":"Fermer le menu");nav?.classList.toggle("is-open",!expanded);});
nav?.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{nav.classList.remove("is-open");toggle?.setAttribute("aria-expanded","false");}));
document.querySelector("#year").textContent=String(new Date().getFullYear());
const recipient=""; // TODO: renseigner et vérifier le courriel de réception avant la mise en production.
document.querySelector("#contact-form")?.addEventListener("submit",(event)=>{
 event.preventDefault();
 const form=event.currentTarget;
 const status=document.querySelector("#form-status");
 if(!form.reportValidity())return;
 if(!recipient){status.textContent="Le formulaire n'est pas encore configuré. Merci de revenir plus tard : aucune demande n'a été envoyée.";return;}
 const data=new FormData(form);
 const subject="Demande de tutorat Paideia — "+String(data.get("level"));
 const body=["Nom : "+data.get("name"),"Courriel : "+data.get("email"),"Niveau : "+data.get("level"),"","Besoins :",""+data.get("message")].join("\n");
 window.location.href="mailto:"+encodeURIComponent(recipient)+"?subject="+encodeURIComponent(subject)+"&body="+encodeURIComponent(body);
 status.textContent="Votre logiciel de courriel devrait s'ouvrir : vérifiez et envoyez le message pour finaliser votre demande.";
});