<template>
    <div class="shadow p-3 mb-5 bg-body rounded">
        <div class="row">
            <div class="col-md-2 offset-md-1 col-3 offset-4 d-flex justify-content-center">
                <img :src="send[8]" width="60px" height="60px" alt="加载失败">
            </div>
            <div class="col-md-6 col-xs-3">
                <div style="height:29px;">
                    <strong style="font-size:20px;">{{ send[1] }}</strong>
                </div>
                <div style="height:30px;">
                    <span class="badge bg-success" style="margin-right:5px;">无广告</span>
                    <span class="badge bg-primary" style="margin-right:5px;">官方</span>
                    <span class="badge bg-info text-dark" style="margin-right:5px;">实用</span>
                </div>
                <div style="height:20px;">
                    <div style="font-size:10px;color:#5E5E5E;">
                        <span style="margin-right:15px;">软件大小: {{ send[3] }}</span>
                        <span style="margin-right:15px;">更新于: {{ send[6] }}</span>
                        <span style="margin-right:15px;">版本: {{ send[4] }}</span>
                    </div>
                </div>
            </div>
            <div class="col-md-3 offset-md-0 col-12 offset-0">
                <div style="height:27px;" class="d-flex justify-content-center">
                    <div data-bs-toggle="modal" data-bs-target="#exampleModal1" class="rounded-pill bg-primary text-light" style="height:27px;width:100px;padding:5px 25px;">
                        <div style="font-size:12px;">
                            <strong>安装教程</strong>
                        </div>
                    </div>
                </div>
                <div style="height:6px;"></div>
                <div data-bs-toggle="modal" href="#exampleModalToggle" style="height:27px;" class="d-flex justify-content-center">
                    <div @click="gotowangpan" data-bs-toggle="modal" data-bs-target="#exampleModal2" class="rounded-pill bg-primary text-light position-relative" style="height:27px;width:100px;padding:5px 35px;">
                        <div style="font-size:12px;">
                            <strong>下载</strong>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row d-none d-md-block" style="height:400px;margin-top:20px;margin-bottom:20px;">
            <div class="col-md-10 offset-md-1">
                <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="@/assets/QQ图片20210510221000.jpg" class="d-block w-100" style="height:400px;" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img src="@/assets/微信图片_20210603215952.jpg" class="d-block w-100" style="height:400px;" alt="...">
                        </div>
                        <div class="carousel-item">
                            <img src="@/assets/微信图片_20210612112341.jpg" class="d-block w-100" style="height:400px;" alt="...">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </div>
        <div class="col-md-10 offset-1">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-chat-square-text" viewBox="0 0 16 16">
                <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-2.5a2 2 0 0 0-1.6.8L8 14.333 6.1 11.8a2 2 0 0 0-1.6-.8H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
                <path d="M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"/>
            </svg>
            特点
        </div>
        <div class="col-md-10 offset-1 fw-light">
            {{ send[5] }}
        </div>
        <div class="col-md-10 offset-1" style="margin-top:20px;">
            <div class="shadow-none p-3 mb-5 bg-light rounded">
                <p>免责声明</p>
                <p>本站提供的一切软件、教程和内容信息仅限用于学习和研究目的；不得将上述内容用于商业或者非法用途，否则，一切后果请用户自负。本站信息来自网络收集整理，版权争议与本站无关。您必须在下载后的24个小时之内，从您的电脑或手机中彻底删除上述内容。如果您喜欢该程序和内容，请支持正版，购买注册，得到更好的正版服务。我们非常重视版权问题，如有侵权请邮件与我们联系处理。敬请谅解！</p>
            </div>
        </div>
        <div class="col-md-10 offset-1" style="margin-top:20px;">
            <span>
                分享
            </span>
            <span style="margin-right:20px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">
                    <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
                </svg>
            </span>
            <span style="margin-right:20px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-twitter " viewBox="0 0 16 16">
                    <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                </svg>
            </span>
            <span style="margin-right:20px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-telegram" viewBox="0 0 16 16">
                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z"/>
                </svg>
            </span>
        </div>
                            <!-- 弹窗1 -->
                            <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog modal-dialog-centered">
                                    <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                                                <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
                                                <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
                                            </svg>
                                            {{ send[1] }}
                                        </h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <div id="model2body" style="visibility:visible">
                                            <div>亲爱的用户，你似乎不是捐赠者或者未登录，所有导致你无法下载，请获取捐赠者权限或者登录之后重试，十分抱歉给您带来了不便</div>
                                        </div>
                                        <div id="model1body" style="visibility:hidden" class="position-absolute top-0 start-0">
                                            <div>在主链接失效的情况下请任意选择备用链接下载</div>
                                            <div><span class="badge bg-primary">百度网盘</span>备用①: <span class="text-primary"  data-bs-toggle="tooltip" data-bs-placement="top" title="请复制前往">{{ this.link }}</span></div>
                                            <div class="text-decoration-line-through"><span class="badge bg-warning text-dark">蓝奏云</span>备用①: <span class="text-warning"  data-bs-toggle="tooltip" data-bs-placement="top" title="请复制前往">{{ this.link }}</span></div>
                                            <div>所有下载链接均失效请联系客服QQ2667955243</div>
                                        </div>
                                    </div>
                                    <div class="modal-footer" style="margin-top:90px;">
                                        <span class="fw-bold" style="margin-right:10px">提取码:{{ this.code }}</span>
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                                        <button id="modelfooter1" @click="gotobaidu" type="button" class="btn btn-primary" style="visibility:hidden">百度云盘</button>
                                        <button type="button" class="btn btn-warning text-dark disabled">蓝奏云</button>
                                    </div>
                                    </div>
                                </div>
                            </div>
                            <!-- 弹窗1 -->
                            <!-- 弹窗2 -->
                            <div class="modal fade" id="exampleModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-dialog-centered">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-arrow-repeat" viewBox="0 0 16 16">
                                            <path d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41zm-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9z"/>
                                            <path fill-rule="evenodd" d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5.002 5.002 0 0 0 8 3zM3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9H3.1z"/>
                                        </svg>
                                        安装教程
                                    </h5>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    下载软件，解压至任意目录下，找到注册机或者进行注册获取注册码，然后打开软件填写注册码 ->一般注册机文件是.exe结尾，软件安装程序是以软件名开头.exe结尾
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>
                                </div>
                                </div>
                            </div>
                            </div>
                            <!-- 弹窗2 -->
    </div>
</template>


<script>





export default {
    props:['send'],
    name:"ClickBody2",
    data(){
        return{
            link:'',
            tip:'',
            code:'',
        }
    },
    methods:{
        gotowangpan:function(){
            this.link = this.send[7];
            this.code = this.send[9];
            let n = this.link.search('http');
            if (n == -1)
            {
                document.getElementById('model1body').style.visibility='hidden';
                document.getElementById('model2body').style.visibility='visible';
                // this.tip = '您是非捐赠者，无法下载捐赠者的资源，如需下载请前往捐赠页面，十分抱歉给您带来了不便'
            }
            else
            {
                document.getElementById('model1body').style.visibility='visible';
                document.getElementById('model2body').style.visibility='hidden';
                document.getElementById('modelfooter1').style.visibility='visible';
            }
        },
        gotobaidu:function(){
           window.open(this.link,'_blank');
        }
    }
}
</script>