var discover_util={
}
$(document).ready(function(){
    $("a.join").on("click",function(e){
        var groupid=$(e.target).attr("data-id");
        $.get("/api/group_join/"+groupid,function(data){
            if(data.fail){
                alert("join fail");
            }else{
                window.location.reload();
            }
        })
    });
    $("a.exit").on("click",function(e){
        var groupid=$(e.target).attr("data-id");
        $.get("/api/group_exit/"+groupid,function(data){
            if(data.fail){
                alert("exit fail");
            }else{
                window.location.reload();
            }
        });
    });
});
