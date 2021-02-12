gsap.registerPlugin(ScrollTrigger);

gsap.to(".motivational-container", {
    backgroundPosition: "50% 100%",
    ease: "none",
    scrollTrigger: {
        trigger: ".motivational-container",
        start: "top bottom",
        end: "bottom top",
        scrub: true,
    }
});


function animateFrom(elem, direction) {
    direction = direction | 1;
    var x = 0,
        y = direction * 100;
    if (elem.classList.contains("gs-reveal-fromLeft")) {
        x = "-50%";
        y = 0;
    } else if (elem.classList.contains("gs-reveal-fromRight")) {
        x = "50%";
        y = 0;
    } else if (elem.classList.contains("gs-reveal-fromBottom")) {
        x = 0;
        y = "-50%"
    }
    gsap.fromTo(elem, { x: x, y: y, autoAlpha: 0, opacity: 0 }, {
        duration: 2,
        x: 0,
        y: 0,
        autoAlpha: 1,
        ease: "expo",
        overwrite: "auto",
        // opacity: 1
    });
}

function hide(elem, direction) {
    direction = direction | -1;
    var x = 0,
        y = 0;

    if (elem.classList.contains("gs-reveal-fromLeft")) {
        x = "-50%";
        y = 0;
    } else if (elem.classList.contains("gs-reveal-fromRight")) {
        x = "50%";
        y = 0;
    } else if (elem.classList.contains("gs-reveal-fromBottom")) {
        x = 0;
        y = "-50%"
    }
    gsap.to(elem, {
        duration: 1.5,
        x: x,
        y: y,
        ease: "sine",
        autoAlpha: 0,
        opacity: 0,
        // markers: true

    })
}

// document.addEventListener("DOMContentLoaded", function () {
//     gsap.registerPlugin(ScrollTrigger);

//     gsap.utils.toArray(".gs-reveal").forEach(function (elem) {
//         hide(elem); // assure that the element is hidden when scrolled into view

//         ScrollTrigger.create({
//             trigger: elem,
//             start: "top bottom-=40%",
//             end:"bottom center-=25%",
//             markers: true,
//             onEnter: function () { animateFrom(elem) },
//             onEnterBack: function () { animateFrom(elem, -1) },
//             onLeave: function () { hide(elem, -1) } 
//         });
//     });
// });

$(document).ready(function () {
    gsap.registerPlugin(ScrollTrigger);

    // gsap.set(".gsap", {xPercent: -100})

    // let tl = gsap.timeline({

    //     scrollTrigger: {
    //         trigger: ".description",
    //         pin: true,
    //         start: "center center",
    //         end: "bottom center-=25%",
    //         scrub: 1,
    //         markers: true,
    //     },
    //     defaults: { duration: 1, ease: 'none' }
    // });
    // tl.from('.gsap', { x: "-100%" })
    // tl.to('.gsap', { x:"100%" }, '+=1')
    // tl.to({}, { duration: 1 })
    gsap.utils.toArray(".gs-reveal").forEach(function (elem) {
        hide(elem, -1);

        ScrollTrigger.create({
            trigger: elem,
            start: "top bottom-=35%",
            end: "bottom center-=28%",
            // toggleAction: "reset none none reset",
            // markers: true,
            onEnter: function () { animateFrom(elem) },
            onEnterBack: function () { animateFrom(elem, -1) },
            onLeave: function () { hide(elem, -1) },
            onLeaveBack: function () { hide(elem, 1) },
        });
        hide(elem, -1);
    });
})
