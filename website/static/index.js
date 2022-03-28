function deleteNumber(noteId) {
    console.log(noteId),
    fetch("/delete-number", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }