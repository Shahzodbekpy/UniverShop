var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		

		if (user == 'AnonymousUser'){
			alert("Agar mahsulot xarid qilmoqchi bo'lsangiz,Ro'yxatdan o'ting...");
		}
		else{
			updateUserOrder(productId,action)
		}
	})
}
function updateUserOrder(productId,action){
	var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}