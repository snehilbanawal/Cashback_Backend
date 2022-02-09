//input
const selectUser = document.getElementById("select-user");
const inputSuggestions = document.querySelector(".input-suggestions");
//input-fields
const inputFields = document.querySelector(".input-fields");
//input-fields li
const inputEntries = document.querySelectorAll(".input-fields li");
//suggestions-fields li
const suggestionsEntries = document.querySelectorAll(".input-suggestions li");

selectUser.addEventListener("keyup", () => {
  inputSuggestions.style.display = "none";
  inputFields.style.display = "block";

  inputEntries.forEach((entry) => {
    const selectedValue = entry.innerHTML;
    entry.addEventListener("click", () => {
      console.log("Hello");
      selectUser.value = selectedValue;
      inputFields.style.display = "none";
    });
  });

  for (let i = 0; i < inputEntries.length; i++) {
    const entry = inputEntries[i];
    var filter = selectUser.value.toUpperCase();
    if (entry.innerHTML.toUpperCase().indexOf(filter) > -1) {
      entry.style.display = "";
    } else {
      entry.style.display = "none";
    }
  }
});
