const tl = gsap.timeline({ default: { ease: "Expo.easeOut" } });
tl.from(".hero-header", {
  duration: 0.5,
  delay: 1,
  opacity: 0,
  x: -200,
  ease: "power1.out",
});
tl.from(".form-group", {
  duration: 0.5,
  opacity: 0,
  y: 150,
  stagger: 0.2,
  ease: "power1.out",
});
tl.from("input.btn.btn-outline", {
  duration: 0.2,
  opacity: 0,
  y: 50,
});

const tl2 = gsap.timeline({ default: { ease: "Expo.easeOut" } });
tl2.from(".cashback-header", {
  duration: 0.5,
  delay: 1,
  opacity: 0,
  x: -200,
});
tl2.fromTo(
  ".cashback-section .container form .form-group",
  {
    duration: 0.5,
    opacity: 0,
    y: 150,
    stagger: 0.2,
  },
  {
    duration: 0.5,
    opacity: 1,
    y: 0,
    stagger: 0.2,
  }
);
tl2.fromTo(
  "input.btn.btn-outline",
  {
    duration: 0.2,
    opacity: 0,
    y: 50,
  },
  {
    duration: 0.2,
    opacity: 1,
    y: 0,
  }
);
