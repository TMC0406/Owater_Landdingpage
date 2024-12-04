$(function () {
    window.onscroll = function () { fun_fix_header() };
    var header = document.getElementById("header");
    var sticky = header.offsetTop;

    // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
    function fun_fix_header() {
        if (window.pageYOffset > sticky) {
            header.classList.add("sticky-header");
        } else {
            header.classList.remove("sticky-header");
        }
    }


    $("#show-more").click(function (e) {
        $("#about-more").slideToggle("slow");
        $(this).hide();
    })


    $(".menu-scrollTop a").click(function (e) {
        e.stopPropagation();
        var e_id = $(this).attr("href");
        console.log(e_id);
        $('html,body').animate({ scrollTop: ($(e_id).offset().top - $("#header").height()) }, 'slow');
    });


    //mobile_menu_trigger
    $('.mobile_menu_trigger').click(function () {
        $(this).find('.nav-icon').toggleClass('active');
        $(".wrap-menu").toggleClass('active');
        $('body').toggleClass('expand-menu');
        header.classList.remove("sticky-header");
    });
    $('.wrap-menu').click(function () {
        $(this).toggleClass('active');
    });
    $('.wrap-m-menu').click(function (e) {
        e.stopPropagation();
    });

    $(".wrap-menu .close-mm").click(function (e) {
        $(".mobile_menu_trigger .nav-icon").toggleClass("active");
        $(".wrap-menu").toggleClass('active');
        e.stopPropagation();
    })

    $('#menu li').bind().click(function (e) {
        $(this).toggleClass("open").find('> ul').stop(true, true).slideToggle(500).end().siblings().find('ul').slideUp().parent().removeClass("open");
        e.stopPropagation();
    });
    $('#menu  a').click(function (e) {
        e.stopPropagation();
    });

    $('.sidebar-menu li').bind().click(function (e) {
        $(this).toggleClass("open").find('.sub').stop(true, true).slideToggle(500).end().siblings().find('.sub').slideUp().parent().removeClass("open");
        e.stopPropagation();
    });
    $('.sidebar-menu li a').click(function (e) {
        e.stopPropagation();
    });




    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    $('#back-to-top').click(function (e) {
        e.stopPropagation();
        $('html,body').animate({ scrollTop: 0 }, 'slow');
    });

});
function printValueForm(idForm) {
	var form = document.getElementById(idForm);
	var inputs = form.querySelectorAll("input");
	inputs.forEach((input) => {
		console.log(input.id + ": " + input.value);
	});
	var textareas = form.querySelectorAll("textarea");
	textareas.forEach((textarea) => {
		console.log(textarea.id + ": " + textarea.value);
	});
}

function numberFormatInput(input) {
	const value = input.value.trim();
	const cleanedValue = value.replace(/[^\d,.-]/g, "");
	const cleanedValueWithComma = cleanedValue.replace(/(,)(?=\d*\.\d*$)/g, "");
	const valueSet = parseFloat(cleanedValueWithComma.replace(/,/g, ""));
	if (!isNaN(valueSet) && isFinite(valueSet) && value !== "") {
		input.value = valueSet;
	} else {
		input.value = "";
	}
}

function handleAddToCart(id) {
    const cartItem = cart.find(item => item.id === id);
    if (cartItem) {
        cartItem.quantity += 1;
        saveCartToLocal(cart);
        updateCartQuantity()
        window.location.href = "/order"
    }
    // alert('Đã thêm sản phẩm vào giỏ hàng!');
}
// Dữ liệu giỏ hàng mặc định
let cart = [
    {
        "id": 1,
        "name": "OWA HIGH OXYGEN TYPE A1",
        "price": 45000,
        "quantity": 0,
        "imgSrc": "/static/assets/imgs/products/Binh nuoc A3.png"
    },
    {
        "id": 2,
        "name": "OWA HIGH OXYGEN TYPE A2",
        "price": 60000,
        "quantity": 0,
        "imgSrc": "/static/assets/imgs/products/Binh nuoc A2.png"
    },
    {
        "id": 3,
        "name": "OWA HIGH OXYGEN TYPE A3",
        "price": 100000,
        "quantity": 0,
        "imgSrc": "/static/assets/imgs/products/Binh nuoc.png"
    }
];
// Khởi tạo giỏ hàng khi tải trang
cart = initializeCart();
document.addEventListener('DOMContentLoaded', () => {
    updateCartQuantity();     
    updateCartTotalDisplay();

});
// Hàm lưu giỏ hàng vào Local Storage
function saveCartToLocal(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Hàm tải giỏ hàng từ Local Storage
function loadCartFromLocal() {
    const storedCart = localStorage.getItem('cart');
    return storedCart ? JSON.parse(storedCart) : null;
}

// Tính tổng giá trị toàn bộ giỏ hàng
function calculateCartTotal(cart) {
    return cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// Hiển thị tổng giá trị giỏ hàng
function updateCartTotalDisplay() {
    const cartTotalElement = document.getElementById('cart-total');
    if (cartTotalElement) {
        const total = calculateCartTotal(cart);
        cartTotalElement.textContent = `Tổng: ${total.toLocaleString('vi-VN')}đ`;
    }
}

// Hàm khởi tạo giỏ hàng
function initializeCart() {
    let localCart = loadCartFromLocal();
    if (!localCart) {
        saveCartToLocal(cart);
        localCart = cart;
    }
    renderCart(localCart);
    return localCart;
}

// Hiển thị danh sách sản phẩm trong giỏ hàng
function renderCart(cart) {
    const container = document.getElementById('cart-container');
    if(!container){
        return
    }  
    
    container.innerHTML = cart.map((item, index) => `
        <tr>
            <td>${index + 1}</td>
            <td class="pro-thumbnail">
                <img style="width: 50px;" src="${item.imgSrc}" alt="${item.name}">
            </td>
            <td class="pro-name">${item.name}</td>
            <td class="pro-price">${item.price.toLocaleString('vi-VN')}đ</td>
            <td>
                <div class="flex">
                    <button onclick="decreaseQuantity(${item.id})" class="btn-style3 h-10 w-10 border p-2 outline-none">
                        <i class="fa-solid fa-minus"></i>
                    </button>
                    <input id="quantity-${item.id}" value="${item.quantity}" readonly class="h-10 outline-none w-20 border p-2 text-center" type="text">
                    <button onclick="increaseQuantity(${item.id})" class="btn-style3 h-10 w-10 border outline-none p-2">
                        <i class="fa-solid fa-plus"></i>
                    </button>
                </div>
            </td>
            <td class="pro-total-price" id="total-${item.id}">${(item.price * item.quantity).toLocaleString('vi-VN')}đ</td>
        </tr>
    `).join('');
    updateTotalCartPrice()
}
// Hàm tính tổng số lượng sản phẩm trong giỏ hàng
function calculateTotalQuantity(cart) {
    return cart.reduce((total, item) => total + item.quantity, 0);
}
// Hàm cập nhật số lượng sản phẩm vào thẻ num-cart
function updateCartQuantity() {
    const numCartElement = document.querySelector('.num-cart');
    if (numCartElement) {
        const totalQuantity = calculateTotalQuantity(cart);
        numCartElement.textContent = totalQuantity; // Cập nhật số lượng
    }
}
// Tăng số lượng sản phẩm
function increaseQuantity(id) {
    const quantityInput = document.getElementById(`quantity-${id}`);
    const cartItem = cart.find(item => item.id === id);
    if (cartItem) {
        cartItem.quantity += 1;
        quantityInput.value = cartItem.quantity;
        updateTotalPrice(cartItem);
        saveCartToLocal(cart);
        updateCartTotalDisplay();
        updateCartQuantity()
        updateTotalCartPrice()
    }

}

// Giảm số lượng sản phẩm
function decreaseQuantity(id) {
    const quantityInput = document.getElementById(`quantity-${id}`);
    const cartItem = cart.find(item => item.id === id);
    if (cartItem && cartItem.quantity > 0) {
        cartItem.quantity -= 1;
        quantityInput.value = cartItem.quantity;
        updateTotalPrice(cartItem);
        saveCartToLocal(cart);
        updateCartTotalDisplay();
        updateCartQuantity()
        updateTotalCartPrice()
    }
}

// Cập nhật tổng giá trị của từng sản phẩm
function updateTotalPrice(item) {
    const totalPriceElement = document.getElementById(`total-${item.id}`);
    if (totalPriceElement) {
        const totalPrice = item.price * item.quantity;
        totalPriceElement.textContent = `${totalPrice.toLocaleString('vi-VN')}đ`;
    }
}
function calculateTotalPrice(cart) {
    return cart.reduce((total, item) => total + item.price * item.quantity, 0);
}
function updateTotalCartPrice() {
    const totalPrice = calculateTotalPrice(cart); // Tính tổng tiền
    const totalCartElement = document.getElementById('totalCart');
    if (totalCartElement) {
        totalCartElement.textContent = `${totalPrice.toLocaleString('vi-VN')}đ`; // Cập nhật giao diện
    }
}
