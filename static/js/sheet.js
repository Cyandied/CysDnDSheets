const tab_buttons = document.querySelectorAll(".tab-button")
const tabs = document.querySelectorAll(".tab")
const last_tab = document.querySelector(".last-tab")

tab_buttons.forEach(tab_button => {
    tab_button.addEventListener("click", e=> {
        const desired_tab = e.target.dataset.tab
        tabs.forEach(tab=>{
            tab.classList.add("hidden")
            if(tab.dataset.tab == desired_tab){
                last_tab.value = desired_tab
                tab.classList.remove("hidden")
            }
        })
    })
})

function forceTab(){
    tabs.forEach(tab=>{
        if(tab.dataset.tab == last_tab.value){
            tab.classList.remove("hidden")
        }
    })
}

window.onload = forceTab()

const search_button = document.querySelectorAll(".search")
const search_params = document.querySelectorAll(".search-for")

const to_sort = document.querySelectorAll(".sortable")

search_button.forEach(button => {
    button.addEventListener("click", e=> {
        for(const param of search_params){
            if(param.value != ""){
                to_sort.forEach(sortable => {
                    let name = sortable.dataset[param.dataset.search]
                    name = name.toLowerCase()
                    sortable.classList.add("hidden")
                    // console.log(name.includes(param.value) + " " + name)
                    // if(name.includes(param.value)){
                    //     sortable.classList.remove("hidden")
                    // }
                })
            }
            else{
                to_sort.forEach(sortable => {
                    sortable.classList.remove("hidden")
                })
            }
        }
    })
})