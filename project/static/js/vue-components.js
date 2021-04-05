Vue.component('sidebar', {
    delimiters: ['[[', ']]'],
    props: [
        'active'
    ],

    mounted(){
        var el = document.getElementById(this.active)
        el.classList.add('active')
    },

    template: 
    `<div class="sidebar mybg-blue-200 mytext-blue-100 text-sm font-bold">
        <div class="sidebar-logo px-8 py-5 mybg-blue-250">
            <img src="/static/media/ef.svg" alt="">
        </div>
        <div class="flex flex-col sidebar-body py-8 px-10 text-base">
            <a href="/" class="pb-5" id="home">Home</a>
            <a href="" class="pb-5" id="works">Works</a>
            <a href="" class="pb-5" id="bugs">Bugs</a>
            <a href="" class="pb-5" id="daily">Daily Reports</a>
            <a href="" class="pb-5" id="users">Users</a>
        </div>
    </div>`
})

Vue.component('navbar', {
    delimiters: ['[[', ']]'],
    props: [
        'id'
    ],
    data: function(){
        return{
            user: {
                first_name: null,
                last_name: null,
                username: null,
            }
        }
    },

    mounted(){
        axios
        .get(`/api/user/${this.id}`)
        .then(res=>this.user=res.data)
    }
})