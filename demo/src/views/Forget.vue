<template>
    <div class="forget" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-lg-4  offset-lg-4 col-md-6 offset-md-3">
                    <div class="shadow p-3 mb-5 bg-body rounded">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="row">
                                    <div class="col-md-12">
                                        <div style="height:50px;">找回密码<hr></div>
                                    </div>
                                    <form class="row" action="">
                                        <div class="col-md-12" style="margin-bottom:10px">
                                            <label for="inputPassword5" class="form-label">用户名</label>
                                            <input onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="text" class="form-control" placeholder="用户名" aria-describedby="passwordHelpBlock" v-model.tirm="username">
                                            <div id="passwordHelpBlock" class="form-text">
                                                需要找回密码的账号
                                            </div>
                                        </div>
                                        <div class="col-md-12">
                                            <label for="inputPassword5" class="form-label">新密码</label>
                                            <input maxlength="16" onkeyup="this.value=this.value.replace(/[^\w_]/g,'');" onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="password" class="form-control" placeholder="密码" aria-describedby="passwordHelpBlock" v-model="password">
                                            <div id="passwordHelpBlock" class="form-text">
                                                密码长度必须是8-20位
                                            </div>
                                        </div>
                                        <div class="col-md-12" style="margin-bottom:10px">
                                            <label for="inputPassword5" class="form-label">邮箱</label>
                                            <input onKeypress="javascript:if(event.keyCode == 32)event.returnValue = false;" type="text" class="form-control" placeholder="注册账号时的邮箱" aria-describedby="passwordHelpBlock" v-model="email">
                                            <div id="passwordHelpBlock" class="form-text"></div>
                                        </div>
                                        <div class="col-md-12" style="margin-bottom:10px">
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
                                        </div>
                                    </form>
                                    <div class="col-md-12">
                                        <div class="bg-primary rounded-3 text-light position-relative d-flex justify-content-center" style="height:40px" @click="forget">
                                            <div id="loadingdh" class="spinner-border text-light" style="visibility:hidden" role="status">
                                                <span class="visually-hidden">Loading...</span>
                                            </div>
                                            <strong id="regdh" class="position-absolute top-50 start-50 translate-middle">确定</strong>
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
    name:'Forget',
    data(){
        return{
            username:'',
            password:'',
            email:'',
            vfcode:'',
            data:{
                code:'',
                msg:'',
            }
        }
    },
    methods:{
        forget:function(){
            let __this = this;
            if (this.username == '')
            {
                alert("请输入用户名")
            }
            else if (this.password == '')
            {
                alert("请输入新密码")
            }
            else if (this.password.length < 8)
            {
                alert("密码位数不能小于8位")
            }
            else if (this.email == '')
            {
                alert("请输入邮箱")
            }
            else
            {   
                document.getElementById('regdh').style.visibility='hidden'  //设置buttom 的注册为 隐藏
                document.getElementById('loadingdh').style.visibility='visible' //设置buttom动画为显示
                let data = {"username":this.username,"password":this.password,"email":this.email,"vfcode":this.vfcode};
                this.$axios.post("http://81.68.105.198:8002/api/v1/fgyz/",data)
                .then(res=>{
                    __this.data = res.data;
                    alert(__this.data.msg);
                    document.getElementById('regdh').style.visibility='visible'  //设置buttom 的注册为 隐藏
                    document.getElementById('loadingdh').style.visibility='hidden' //设置buttom动画为显示
                    if (__this.data.code == "1000"){
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
                alert("请输入新密码")
            }
            else if (this.password.length < 8)
            {
                alert("密码位数不能小于8位")
            }
            else if (this.email == '')
            {
                alert("请输入邮箱")
            }
            else
            {
                document.getElementById('senddh').style.visibility='hidden'  // 设置buttom 的发送为 隐藏
                document.getElementById('loadingdh2').style.visibility='visible' //设置buttom动画为显示
                let data = {"username":this.username,"email":this.email};
                this.$axios.post("http://81.68.105.198:8002/api/v1/fgfs/",data)
                .then(res=>{
                    __this.data = res.data;
                    alert(__this.data.msg);
                    document.getElementById('senddh').style.visibility='visible'  // 设置buttom 的发送为 显示
                    document.getElementById('loadingdh2').style.visibility='hidden' //设置buttom动画为隐藏
                })
            }
            
        }
    },
    mounted(){
        
    }
}
</script>