window.addEventListener("scroll",()=>{

    console.log("Scrolling");

});



// home hero section
function openForm(){

    document.getElementById("popup").style.display = "flex";

}

function closeForm(){

    document.getElementById("popup").style.display = "none";

}

// home continue button

function showSuccess(){

    alert("Welcome to EdTech 🚀");

    document.getElementById("popup").style.display = "none";

}



// home power section
function showExploreMsg(event){

    event.preventDefault(); // link jump aagatha stop pannum

    document.getElementById("msg").innerHTML =
    "Explore more courses and improve your skills 🚀";

}


// home courses section
function openModal(title, text){

    document.getElementById("modalTitle").innerText = title;

    document.getElementById("modalText").innerText = text;

    document.getElementById("courseModal").style.display = "flex";
}



function closeModal(){

    document.getElementById("courseModal").style.display = "none";
}

/* OUTSIDE CLICK CLOSE */

window.onclick = function(event){

    let modal = document.getElementById("courseModal");

    if(event.target === modal){

        modal.style.display = "none";
    }
}



// courses details section
const favBtn=document.getElementById("fav-btn");

if(favBtn){

    favBtn.addEventListener("click",()=>{

        alert("Added To Favorites");

    });

}



// quiz quiz section
const timer=document.getElementById("timer");

if(timer){

    let time=60;

    setInterval(()=>{

        if(time>0){

            time--;

            timer.innerText=time;

        }

    },1000);

}