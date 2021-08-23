<template>
    <div class="register" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-md-8  offset-md-2">
                    <div class="shadow p-3 mb-5 bg-body rounded">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="row">
                                    <div class="col-md-12">
                                        <div style="height:50px;">注册<hr></div>
                                    </div>
                                    <form class="row" action="">
                                        <div class="col-md-6" style="margin-bottom:10px">
                                            <label for="inputPassword5" class="form-label">用户名</label>
                                            <input maxlength="16" onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="text" class="form-control" placeholder="用户名" aria-describedby="passwordHelpBlock" v-model.tirm="username">
                                            <div id="passwordHelpBlock" class="form-text">
                                                用户名只能是数字、大小写字母和下划线
                                            </div>
                                        </div>
                                        <div class="col-md-6" style="margin-bottom:10px"></div>
                                        <div class="col-md-6">
                                            <label for="inputPassword5" class="form-label">密码</label>
                                            <input maxlength="16" onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="password" class="form-control" placeholder="密码" aria-describedby="passwordHelpBlock" v-model="password">
                                            <div id="passwordHelpBlock" class="form-text">
                                                密码长度必须是8-16位,且只能输入数字和大小写字母
                                            </div>
                                        </div>
                                        <div class="col-md-6" style="margin-bottom:10px">
                                            <label for="inputPassword5" class="form-label">重复密码</label>
                                            <input onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="password" class="form-control" placeholder="重复密码" aria-describedby="passwordHelpBlock" v-model="repassword">
                                            <div id="passwordHelpBlock" class="form-text">
                                                请重复密码
                                            </div>
                                        </div>
                                        <div class="col-md-6" style="margin-bottom:10px">
                                            <label for="inputPassword5" class="form-label">邮箱</label>
                                            <input  onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="text" class="form-control" placeholder="任意邮箱" aria-describedby="passwordHelpBlock" v-model="email">
                                            <div id="passwordHelpBlock" class="form-text"></div>
                                        </div>
                                        <div class="col-md-6"></div>
                                        <div class="col-md-6" style="margin-bottom:10px">
                                            <div class="input-group col-mb-3">
                                                <input onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="text" class="form-control" placeholder="邮箱验证码" aria-label="Recipient's username" aria-describedby="button-addon2" v-model="vfcode">
                                                <button class="btn btn-outline-secondary bg-primary text-light" type="button" id="button-addon2" @click="sendout" >
                                                    <div id="senddh" class="position-absolute top-50 start-50 translate-middle" style="visibility:visible">发送</div>
                                                    <div id="loadingdh2" class="spinner-border text-light" style="visibility:hidden" role="status">
                                                        <span class="visually-hidden">Loading...</span>
                                                    </div>
                                                </button>
                                            </div>
                                        </div>
                                        <div class="col-md-12" style="margin-bottom:10px">
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="flexCheckIndeterminate" v-model="checked">
                                                <label class="form-check-label" for="flexCheckIndeterminate">
                                                    注册即代表同意
                                                    <a href="#/agreement">服务条款</a>
                                                </label>
                                            </div>
                                        </div>
                                    </form>
                                    <div class="col-md-12">
                                        <div class="bg-primary rounded-3 text-light position-relative d-flex justify-content-center" style="height:40px" @click="register">
                                            <div id="loadingdh" class="spinner-border text-light" style="visibility:hidden" role="status">
                                                <span class="visually-hidden">Loading...</span>
                                            </div>
                                            <strong id="regdh" class="position-absolute top-50 start-50 translate-middle" style="visibility:visible">注册</strong>
                                            
                                        </div>
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
        </div>
    </div>
</template>


<script>
export default {
    name:'Signin',
    data(){
        return{
            checked:false,
            username:'',
            password:'',
            repassword:'',
            email:'',
            vfcode:'',
            data:{
                code:'',
                msg:'',
            }
        }
    },
    methods:{
        register:function(){
            let __this = this;
            if (this.username == '')
            {
                alert("请输入用户名")
            }
            else if (this.password.length < 8)
            {
                alert("密码位数不能小于8位")
            }
            else if (this.password != this.repassword)
            {
                alert("两次密码不一致")
            }
            else if (this.email == '')
            {
                alert("请输入邮箱")
            }
            else if (this.checked == false)
            {
                alert("请同意服务条款")
            }
            else
            {   
                document.getElementById('regdh').style.visibility='hidden'  //设置buttom 的注册为 隐藏
                document.getElementById('loadingdh').style.visibility='visible' //设置buttom动画为显示
                let data = {"username":this.username,"password":this.password,"email":this.email,"vfcode":this.vfcode};
                this.$axios.post("http://81.68.105.198:8002/api/v1/yz/",data)
                .then(res=>{
                    __this.data = res.data;
                    alert(__this.data.msg);
                    document.getElementById('regdh').style.visibility='visible'  //设置buttom 的注册为 隐藏
                    document.getElementById('loadingdh').style.visibility='hidden' //设置buttom动画为显示
                    if (__this.data.code == "1000"){
                        // window.location.href="http://172.20.10.4:8080/#/signin";
                        window.location.href="http://81.68.105.198:70/#/signin";
                    }
                })
            }
        },
        sendout:function(){
            let __this = this;
            if (this.username == '')
            {
                alert("请输入用户名")
            }
            else if (this.password == '')
            {
                alert("请输入密码")
            }
            else if (this.password.length < 8)
            {
                alert("密码位数不能小于8位")
            }
            else if (this.password != this.repassword)
            {
                alert("两次密码不一致")
            }
            else if (this.email == '')
            {
                alert("请输入邮箱")
            }
            else if (this.checked == false)
            {
                alert("请同意服务条款")
            }
            else
            {
                document.getElementById('senddh').style.visibility='hidden'  // 设置buttom 的发送为 隐藏
                document.getElementById('loadingdh2').style.visibility='visible' //设置buttom动画为显示
                let data = {"email":this.email};
                this.$axios.post("http://81.68.105.198:8002/api/v1/fs/",data)
                .then(res=>{
                    __this.data = res.data;
                    alert(__this.data.msg);
                    document.getElementById('senddh').style.visibility='visible'  // 设置buttom 的发送为 显示
                    document.getElementById('loadingdh2').style.visibility='hidden' //设置buttom动画为隐藏
                    // if (__this.data.code == "1000"){
                    //     window.location.href="http://172.20.10.4:8080/#/";
                    // }
                })
            }
            
        }
    },
    mounted(){
        
    }
}
</script>