$(document).ready(function(){
                $("[data-toggle='popover']").popover();
                $("#logout").on('click',function(){
                    var url = '/logout_cgi';
                    $.post(url,function(json){
                        if(json.ret == 0){
                            window.location.href = "/login";
                        }else{
                            alert("退出失败，请重试！")
                        }
                    },'json')
                });
            });