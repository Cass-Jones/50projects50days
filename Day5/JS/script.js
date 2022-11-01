const bg = document.querySelector(".bg");
const loadText = document.querySelector(".loading-text");

let load = 0;

const blurring = () => {
  load++;
  if (load > 99) {
    clearInterval(int);
  }
  console.log(load);

  loadText.innerText = `${load}%`;
  loadText.style.opacity = scale(load, 0, 100, 1, 0);
  bg.style.filter = `blur(${scale(load, 0, 100, 30, 0)}px)`;
};

function scale(num, inMin, inMax, outMin, outMax) {
  return ((num - inMin) * (outMax - outMin)) / (inMax - inMin) + outMin;
}

let int = setInterval(blurring, 30);
