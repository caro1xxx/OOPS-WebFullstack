<template>
  <div class="user" style="margin-top: 60px;">
    <div class="container">
        <div class="row">
            <div class="col-md-12" style="height:400px;">
                <div class="shadow p-3 bg-body rounded center1"  style="height:370px;">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="position-relative">
                                <div class="row">
                                    <img src="@/assets/user.png" style="height:300px;max-width:100%;" alt="">
                                    <span class="position-absolute bottom-0 start-50 translate-middle-x grad1">
                                        <div class="row">
                                            <div class="col-md-1 d-none d-lg-block">
                                                <div class="rounded-circle" style="height:70px;width:70px;background-color:#ffffff">
                                                    
                                                </div>
                                            </div>
                                            <div class="col-md-5">
                                                <div style="height:10px;"></div>
                                                <div style="height:30px;">
                                                    <strong style="color:#ffffff;font-size:20px">{{ $store.state.data.username}}</strong>
                                                </div>
                                                <div style="height:30px;">
                                                    <span class="badge bg-info text-dark" style="margin-right:10px;">{{ $store.state.data.isattribute }}</span>
                                                    <span class="badge bg-success" style="margin-right:10px;">安全</span>
                                                    <span class="badge bg-dark" style="margin-right:10px;">{{ $store.state.data.isdonor}}</span>
                                                </div>
                                                <div style="height:10px;"></div>
                                            </div>
                                        </div>
                                    </span>
                                </div>
                            </div>
                            <div>
                                <div style="height:50px">
                                    <div class="row">
                                        <ul style="list-style:none;">
                                            <li class="col-md-1" style="float:left;">
                                                <div class="row" style="height:50px">
                                                    <div class="col-md-3"></div>
                                                    <div class="col-md-5" style="padding-top:10px;">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                                            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                                                            <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </li>
                                            <li class="col-md-1" style="float:left;">
                                                <div class="row" style="height:50px">
                                                    <div class="col-md-3"></div>
                                                    <div class="col-md-5" style="padding-top:10px;">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
                                                            <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2zm13 2.383-4.758 2.855L15 11.114v-5.73zm-.034 6.878L9.271 8.82 8 9.583 6.728 8.82l-5.694 3.44A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.739zM1 11.114l4.758-2.876L1 5.383v5.73z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </li>
                                            <li class="col-md-1" style="float:left;">
                                                <div class="row" style="height:50px">
                                                    <div class="col-md-3"></div>
                                                    <div class="col-md-5" style="padding-top:10px;">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                                                            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </li>
                                            <li class="col-md-1" style="float:left;">
                                                <div class="row" style="height:50px">
                                                    <div class="col-md-3"></div>
                                                    <div class="col-md-5" style="padding-top:10px;">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear" viewBox="0 0 16 16">
                                                            <path d="M8 4.754a3.246 3.246 0 1 0 0 6.492 3.246 3.246 0 0 0 0-6.492zM5.754 8a2.246 2.246 0 1 1 4.492 0 2.246 2.246 0 0 1-4.492 0z"/>
                                                            <path d="M9.796 1.343c-.527-1.79-3.065-1.79-3.592 0l-.094.319a.873.873 0 0 1-1.255.52l-.292-.16c-1.64-.892-3.433.902-2.54 2.541l.159.292a.873.873 0 0 1-.52 1.255l-.319.094c-1.79.527-1.79 3.065 0 3.592l.319.094a.873.873 0 0 1 .52 1.255l-.16.292c-.892 1.64.901 3.434 2.541 2.54l.292-.159a.873.873 0 0 1 1.255.52l.094.319c.527 1.79 3.065 1.79 3.592 0l.094-.319a.873.873 0 0 1 1.255-.52l.292.16c1.64.893 3.434-.902 2.54-2.541l-.159-.292a.873.873 0 0 1 .52-1.255l.319-.094c1.79-.527 1.79-3.065 0-3.592l-.319-.094a.873.873 0 0 1-.52-1.255l.16-.292c.893-1.64-.902-3.433-2.541-2.54l-.292.159a.873.873 0 0 1-1.255-.52l-.094-.319zm-2.633.283c.246-.835 1.428-.835 1.674 0l.094.319a1.873 1.873 0 0 0 2.693 1.115l.291-.16c.764-.415 1.6.42 1.184 1.185l-.159.292a1.873 1.873 0 0 0 1.116 2.692l.318.094c.835.246.835 1.428 0 1.674l-.319.094a1.873 1.873 0 0 0-1.115 2.693l.16.291c.415.764-.42 1.6-1.185 1.184l-.291-.159a1.873 1.873 0 0 0-2.693 1.116l-.094.318c-.246.835-1.428.835-1.674 0l-.094-.319a1.873 1.873 0 0 0-2.692-1.115l-.292.16c-.764.415-1.6-.42-1.184-1.185l.159-.291A1.873 1.873 0 0 0 1.945 8.93l-.319-.094c-.835-.246-.835-1.428 0-1.674l.319-.094A1.873 1.873 0 0 0 3.06 4.377l-.16-.292c-.415-.764.42-1.6 1.185-1.184l.292.159a1.873 1.873 0 0 0 2.692-1.115l.094-.319z"/>
                                                        </svg>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="shadow p-3 mb-5 bg-body rounded">
            <hr>
            <div class="row">
                <div class="mb-3 row">
                    <label for="staticEmail" class="col-sm-2 col-form-label">账号</label>
                    <div class="col-sm-10">
                        {{ $store.state.data.username }}
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 row">
                    <label for="staticEmail" class="col-sm-2 col-form-label">邮箱</label>
                    <div class="col-sm-10">
                        {{ $store.state.data.email }}
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="mb-3 row">
                    <label for="staticEmail" class="col-sm-2 col-form-label">注册时间</label>
                    <div class="col-sm-10">
                        {{ $store.state.data.create_time }}
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12 d-flex justify-content-center">
                <small style="font-size:10px">Copyright &copy; 2021 OOPS</small>
            </div>
        </div>
    </div>
  </div>
</template>



<script>
export default {
    name:'User',
    data(){
        return{
            // username:this.$store.state.data.username,
            // email:this.$store.state.data.email,
            // create_time:this.$store.state.data.create_time,
        }
    },
    mounted(){
        // 查看cookies
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
    }


}
</script>

<style>
.grad1{
    opacity: 0.8;
    height: 80px;
    background-image: linear-gradient(#ffffff00, #000000c7);
}
</style>