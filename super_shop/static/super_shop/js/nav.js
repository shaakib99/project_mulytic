document.onclick = (e) => {
    const category_list = document.getElementById('category-list')
    const hierchy = e.path
    for(var i=0; i< hierchy.length;i++){
        if(hierchy[i].className === 'nav-cat'){
            const sts = category_list.style.visibility 
            category_list.style.visibility = sts === 'visible' ? 'hidden' : 'visible'
            return
        }
    }
    category_list.style.visibility = 'hidden'
}