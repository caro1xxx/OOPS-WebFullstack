<template>
    <div class="signin" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-lg-10  offset-lg-1 col-md-6 offset-md-3">
                    <div class="shadow p-3 mb-5 bg-body rounded">
                        <div class="row">
                            <div class="col-lg-4 col-md-12">
                                <div style="height:50px;">登录<hr></div>
                                <div style="height:50px;font-size:30px;">
                                    欢迎使用OOPS
                                </div>
                                <div style="height:50px;"></div>
                                <form action="">
                                    <div style="height:200px;">
                                    <div class="mb-3">
                                        <label class="form-label">用户名</label>
                                        <input maxlength="16" onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="text" class="form-control" id="formGroupExampleInput" placeholder="请输入用户名" v-model="username">
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label">密码</label>
                                        <input maxlength="16" onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="password" class="form-control" id="formGroupExampleInput2" placeholder="请输入密码" v-model="password">
                                    </div>
                                </div>
                                <div style="height:50px;">
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate" v-model="remembercheckbox">
                                        <label class="form-check-label" for="flexCheckIndeterminate">
                                            记住我
                                        </label>
                                    </div>
                                </div>
                                </form>
                                <div style="height:50px;">
                                    <div style="height:50px;float:left;">
                                        <div style="margin:10px">
                                            <router-link to="/Forget">忘记密码?</router-link>
                                        </div>
                                    </div>
                                    <div style="height:50px;float:right;">
                                        <button type="submit" class="btn btn-primary" @click="login">登录</button>
                                    </div>
                                </div>
                                <div style="height:50px;" class="d-flex justify-content-center">
                                    <router-link to="/Register" class="nav-link diyfont">注册账号</router-link>
                                </div>
                            </div>
                            <div class="col-md-8 d-none d-lg-block">
                                <img src="@/assets/微信图片_20210801111621.jpg" style="height:500px;max-width:100%;" alt="">
                            </div>
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
    name:'Signin',
    data(){
        return{
            remembercheckbox:false,
            username:'',
            password:'',
            data:{
                code:'',
                msg:'',
                token:'',
            }
        }
    },
    methods:{
        login:function(){
            let __this = this;
            if (this.username == '')
            {
                alert("请输入用户名")
            }
            else if (this.password == '')
            {
                alert("请输入密码")
            }
            else
            {
                let data = {"username":this.username,"password":this.password};
                this.$axios.post("http://81.68.105.198:8002/api/v1/auth/",data)
                .then(res=>{
                    __this.data = res.data;
                    alert(__this.data.msg);
                    if (__this.data.code == "1000"){
                        // 判断是否点记住我
                        if (__this.remembercheckbox == false)
                        {
                            this.$cookies.set('token',this.data.token,60*60*24);
                            window.location.href="http://81.68.105.198:70/#/";
                            this.$router.go(0)
                        }
                        else 
                        {
                            this.$cookies.set('token',this.data.token,60*60*24*14);
                            window.location.href="http://81.68.105.198:70/#/";
                            this.$router.go(0)
                        }
                        
                    }
                })
            }
        }
    },
}

</script>