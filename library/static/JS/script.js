document.addEventListener("DOMContentLoaded", function () {
  // ===== Modal Control =====
  const modals = document.querySelectorAll(".modal");
  const spans = document.querySelectorAll(".close");

  spans.forEach((span) => {
    span.onclick = () =>
      (span.parentElement.parentElement.style.display = "none");
  });

  window.onclick = (event) => {
    if (event.target.classList.contains("modal")) {
      event.target.style.display = "none";
    }
  };

  // ===== Tìm sách theo ID =====
  document
    .getElementById("searchByIdBtn")
    .addEventListener("click", function (e) {
      e.preventDefault();
      const bookId = document.getElementById("searchBookId").value.trim();
      const resultDiv = document.getElementById("resultDiv");

      if (!bookId) {
        resultDiv.innerText = "Vui lòng nhập ID!";
        return;
      }

      fetch(`/book_management/get_book/${bookId}`)
        .then(handleResponse)
        .then((data) => displayBook(data, resultDiv))
        .catch(handleError(resultDiv));
    });

  // ===== Tìm sách theo tên =====
  document
    .getElementById("searchByNameBtn")
    .addEventListener("click", function (e) {
      e.preventDefault();
      const bookName = document.getElementById("searchBookName").value.trim();
      const resultDiv = document.getElementById("resultDiv");

      if (!bookName) {
        resultDiv.innerText = "Vui lòng nhập tên!";
        return;
      }

      fetch(`/book_management/search_book/${encodeURIComponent(bookName)}`)
        .then((response) => response.json())
        .then((books) => {
          let html = "<h3>Kết quả:</h3>";
          if (books.length === 0) {
            html += "<p>Không tìm thấy sách!</p>";
          } else {
            books.forEach((book) => {
                html += `<p>Tên Sách: ${book.ten}</p>`;
                html += `<p>ID: ${book.id}</p>`;
                html += `<p>Số Trang: ${book.soTrang}</p>`;
            });
          }
          resultDiv.innerHTML = html;
        })
        .catch(handleError(resultDiv));
    });

  // ===== Thêm sách =====
document.getElementById("them_sach").addEventListener("click", () => {
    document.getElementById("addModal").style.display = "block";
  });
  
  document.getElementById("confirmAdd").addEventListener("click", () => {
    const data = {
      ten: document.getElementById("tenSach").value,
      soTrang: document.getElementById("soTrang").value,
    };
  
    fetch("/book_management/add_book", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    })
      .then((response) => response.text())
      .then((result) => {
        alert(result);
        document.getElementById("addModal").style.display = "none";
      })
      .catch((error) => console.error("Lỗi:", error));
  });
  

  // ===== Xoá sách =====
  const deleteButtons = ["deleteByIdBtn", "deleteByNameBtn"];
  deleteButtons.forEach((btnId) => {
    document.getElementById(btnId).addEventListener("click", function () {
      document.getElementById("deleteModal").style.display = "block";
      const deleteType = btnId.includes("Id") ? "id" : "ten";

      document.getElementById("confirmDelete").onclick = () => {
        const value = document.getElementById("deleteValue").value.trim();
        let endpoint = "";
        if (deleteType === "id") {
          endpoint = `/book_management/delete_book/${value}`;
        } else {
          endpoint = `/book_management/delete_book/${encodeURIComponent(
            value
          )}`;
        }

        fetch(endpoint, { method: "DELETE" })
          .then((response) => response.text())
          .then((result) => {
            alert(result);
            document.getElementById("deleteModal").style.display = "none";
          })
          .catch((error) => console.error("Lỗi:", error));
      };
    });
  });

  // ===== Cập nhật sách =====
  document.getElementById("updateBookBtn").addEventListener("click", () => {
    document.getElementById("updateModal").style.display = "block";
  });

  document.getElementById("confirmUpdate").addEventListener("click", () => {
    const updateData = {
      id: document.getElementById("updateId").value,
      ten: document.getElementById("newTen").value,
      soTrang: document.getElementById("newSoTrang").value,
    };

    fetch(`/book_management/update_book/${updateData.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updateData),
    })
      .then((response) => response.text())
      .then((result) => {
        alert(result);
        document.getElementById("updateModal").style.display = "none";
      })
      .catch((error) => console.error("Lỗi:", error));
  });

  // ===== Xem tất cả sách =====
  document
    .getElementById("viewAllBooksBtn")
    .addEventListener("click", function (e) {
      e.preventDefault();
      const resultDiv = document.getElementById("allBooksResult");

      fetch("/book_management/get_all_book")
        .then((response) => {
          const contentType = response.headers.get("content-type");
          return contentType && contentType.includes("application/json")
            ? response.json()
            : response.text();
        })
        .then((data) => {
          let html =
            '<h3 style="text-align: center; font-size:20px;font-weight:bold; ">Tất cả sách có trong kho:</h3>';
          if (typeof data === "object" && Array.isArray(data)) {
            if (data.length === 0) {
              html += "<p>Không có sách nào!</p>";
            } else {
              data.forEach((book) => {
                html += `<p>Tên Sách: ${book.ten}</p>`;
                html += `<p>ID: ${book.id}</p>`;
                html += `<p>Số Trang: ${book.soTrang}</p>`;
                html += `<p>-----------------------------</p>`;
              });
            }
          } else {
            html += `<p>${data}</p>`;
          }
          resultDiv.innerHTML = html;
        })
        .catch((error) => {
          console.error("Lỗi:", error);
          resultDiv.innerText = "Có lỗi xảy ra!";
        });
    });

  // ===== Hàm hỗ trợ =====
  function handleResponse(response) {
    const contentType = response.headers.get("content-type");
    return contentType && contentType.includes("application/json")
      ? response.json()
      : response.text();
  }

  function displayBook(data, element) {
    if (typeof data === "object") {
      element.innerHTML = `
                <h3>Thông tin sách:</h3>
                <p>Tên: ${data.ten || "N/A"}</p>
                <p>Số trang: ${data.soTrang || "N/A"}</p>
            `;
    } else {
      element.innerText = data;
    }
  }

  function handleError(element) {
    return (error) => {
      console.error("Lỗi:", error);
      element.innerText = "Có lỗi xảy ra!";
    };
  }
});
