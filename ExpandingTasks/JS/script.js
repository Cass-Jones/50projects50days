const tasks = document.querySelectorAll(".task");

tasks.forEach((task) => {
  const activeButton = task.querySelector(".showDetails");
  const taskDetails = task.querySelector(".task-details");
  activeButton.addEventListener("click", () => {
    activeButton.classList.toggle("showing");
    taskDetails.classList.toggle("active");
  });
});

const expandAll = document.querySelector(".expandAll");
const collapseAll = document.querySelector(".collapseAll");

expandAll.addEventListener("click", () => {
  tasks.forEach((task) => {
    const taskDetails = task.querySelector(".task-details");
    taskDetails.classList.add("active");
  });
});
collapseAll.addEventListener("click", () => {
  tasks.forEach((task) => {
    const taskDetails = task.querySelector(".task-details");
    taskDetails.classList.remove("active");
  });
});
