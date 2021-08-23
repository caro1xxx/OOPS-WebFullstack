<template>
    <div class="about" style="margin-top:90px;">
        <div class="container">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <div class="shadow p-3 mb-5 bg-body rounded">
                        <div>
                            <img src="@/assets/OOPS.png" style="height:30px;" alt="">
                                <hr>
                                <div class="fw-light row">
                                    <p>关于OOPS</p>
                                    <span>OOPS是我在闲暇时间无聊打发时间也正好练练手的项目，目前使用到的技术Python的后端框架Django作为后端；前端使用的Vue框架外加bootstrap框架，因为使用了bootstrap框架暂时UI还是比较合我心意。这是一个前后端分离的项目，所以后端Django采用的RESTful风格，使用了Django rest framework框架，待日后项目完善了我会将这个项目在Github上面开源，关于OOPS就这样差不多了</span>
                                    <p>有兴趣的可以关注微信公众号，不定时更新实用工具和新奇百科</p>
                                    <div class="col-md-4 offset-md-1">
                                        <img src="@/assets/oopsaiya.jpg" width="150px" height="150px" alt="加载失败">
                                    </div>
                                </div>
                                <hr>
                                
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
</template>



<script>
export default {
  name:"About",
  data(){
      return{

      }
  },
}
</script>