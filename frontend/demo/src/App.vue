<template>
    <div id="app" class="position-relative"> 
        <div style="z-index:1;">
            <nav class="navbar navbar-expand-md navbar-white  bg-white fixed-top border-bottom" style="height:60px">
                        <!-- logo -->
                        <div class="container-fluid bg-white" style="z-index:1;">
                            <img src="../src/assets/OOPS.png" alt="Logo" class="diylogoset">
                        <!-- nav -->
                        <!-- collapsibe Button -->
                        <button class="navbar-toggler  bg-primary" type="button " data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded='false'  aria-label="Toggle navigation">
                            <!-- <span class="navbar-toggler-icon"></span> -->
                            <span><img src="@/assets/menu.png" width="30px" height="30px" alt="加载失败"></span>
                        </button>
                        <!-- link -->
                        <keep-alive>
                        <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
                            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                            <li class="nav-item"  @click="gotoabc">
                                <router-link to="/" class="nav-link diyfont" aria-current="page">首页</router-link>
                            </li>
                            <li class="nav-item" @click="gotoabc">
                                <router-link to="/more/1" class="nav-link diyfont">更多</router-link>
                            </li>
                            <li class="nav-item" @click="gotoabc">
                                <router-link :class="{disabled:$store.state.data.isdisabled}" to="/user" class="nav-link diyfont">账号</router-link>
                            </li>
                            <li class="nav-item" @click="gotoabc">
                                <router-link to="/signin" class="nav-link diyfont">登录</router-link>
                            </li>
                            <li class="nav-item" @click="gotoabc">
                                <router-link to="/donation" class="nav-link diyfont">捐赠</router-link>
                            </li>
                            <li class="nav-item" @click="gotoabc">
                                <router-link to="/about" class="nav-link diyfont">关于</router-link>
                            </li>
                            </ul>
                            <div class="d-flex justify-content-center" style="padding-top:5px;height:50px;width:60px;">
                                <div class="rounded-circle d-flex justify-content-center bg-primary" style="height:40px;width:40px;padding:5px 0px;">
                                    <svg v-show=$store.state.data.seen1 xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-dash" viewBox="0 0 16 16">
                                        <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H1s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C9.516 10.68 8.289 10 6 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
                                        <path fill-rule="evenodd" d="M11 7.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5z"/>
                                    </svg>
                                    <svg v-show=$store.state.data.seen2 xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-check" viewBox="0 0 16 16">
                                        <path d="M6 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H1s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C9.516 10.68 8.289 10 6 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
                                        <path fill-rule="evenodd" d="M15.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 0 1 .708-.708L12.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                                    </svg>
                                </div>                 
                            </div>
                            <form class="d-flex" style="margin:10px">
                                <input onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" class="form-control me-2" type="search" placeholder="请输入搜索内容" aria-label="Search" v-model="searchcontent">
                                <button @click="search" class="btn btn-outline-primary" type="submit">Search</button>
                            </form>
                        </div>
                        </keep-alive>
                    </div>
            </nav>
            <div class="diybackgroundset">
                <keep-alive>
                    <router-view/>
                </keep-alive>
            </div>
        </div>
        <!-- <div class="fixed-top">
            <div class="position-relative container-fluid" style="z-index:3;">
                <div class="row">
                    <div class="d-flex justify-content-center" style="background-color:#c7ebfacc;" :style="{height:sreanmheight + 'px',width:sreanmwidth + 'px'}">
                        <div class="spinner-border text-primary" role="status" style="margin-top:50px;">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
        </div> -->
    </div>
</template>

// position-absolute top-0 start-50 translate-middle-x

<script>
export default {
    name:'App',
    data(){
        return{
            sreanmheight:Number,
            sreanmwidth:Number,
            seen1:true,
            seen2:false,
            is:false,
            searchcontent:'',
        }
    },
    mounted(){
        this.sreanmheight = document.body.clientHeight;
        this.sreanmwidth = document.body.clientWidth;
        let istoken = this.$cookies.isKey('token');
        if (istoken == true)
        {
            let __this = this;
            let data = {"token":this.$cookies.get('token')};
            this.$axios.post('http://81.68.105.198:8002/api/v1/TokenAuthView/',data)
            .then(function(response){
            __this.$store.commit('GetUserInfo',response.data.data);
            })
            .catch(function (error){
            console.log(error);
            });
        }
    },
    methods:{
        // 导航栏收回
        gotoabc:function(){
            if (this.sreanmwidth <= 600)
            {
                document.getElementById('navbarTogglerDemo02').className +='show';
            }
        },
        // 搜索
        search:function(){
            if (this.searchcontent == '')
            {
                alert('请输入搜索关键字')
            }
            else
            {
                window.open(`http://81.68.105.198:70/#/search/${this.searchcontent}`)
            }
        }
    }
}

</script>