var group_util={
    listTemplateHTML:'<li><label data-groupid="<%=groupid%>" data-groupname="<%=groupname%>">'+
        '<input class="groupselect" name="groupselect" type="radio"/>'+
        '<%=groupname%>'+
        '</label></li>',
    bind:function(){
        $("ul#group").html("");
        for(var i=0;i<group_data.length;i++){
            var groupname=group_data[i].groupname;
            var listHTML=_.template(group_util.listTemplateHTML)({
                groupname:group_data[i].groupname,
                groupid:group_data[i].groupid
            });
            $("ul#group").append(listHTML);
        }
        $("button#addgroup").on("click",function(){
            var groupname=$("#groupname").val();
            $.post("/api/add_group", {
                groupname:groupname
            },
                   function(data){
                       if(data.fail){
                           alert("update fail");
                       }else{
                           var listHTML=_.template(group_util.listTemplateHTML)({
                               groupname:groupname,
                               groupid:data.id
                           });
                           $("ul#group").append(listHTML);
                       }
                   });
        });
        $("ul#group").click(function(e){
            var $input=$(e.target).closest("input[name=groupselect]");
            if($input.length==1){
                var $label=$input.closest("label");
                var groupname=$label.attr("data-groupname");
                var groupid=$label.attr("data-groupid");
                selected_data.groupid=groupid;
                $.get("/api/group_get_member/"+groupid,function(data){
                    group_member_util.render(data);
                });
            }
        });
    },
}
var group_member_util={
    listTemplateHTML:"<li><h4><%=username%>&nbsp;&nbsp&nbsp"+
        '<a class="delmember" data-id="<%=userid%>">Del</a></h4></li>',
    bind:function(){
        $("ul#memberlist").click(function(e){
            var groupid=selected_data.groupid;
            if(!groupid){
                return ;
            }
            var $a=$(e.target).closest("a.delmember");
            if($a.length==1){
                var userid=$a.attr("data-id");
                $.get("/api/group_del_member/"+groupid+"/"+userid,function(data){
                    if(data.fail){
                        console.log("del fail");
                    }else{
                        group_member_util.delRender({
                            userid:userid
                        });
                    }
                });
            }
        });
    },
    render:function(data){
        $("ul#memberlist").html("");
        _.each(data,function(user){
            var html=_.template(group_member_util.listTemplateHTML)(user);
            $("ul#memberlist").append(html);
        });
    },
    addRender:function(user){
        var html=_.template(group_member_util.listTemplateHTML)(user);
        $("ul#memberlist").append(html);
    },
    delRender:function(user){
        $("ul#memberlist a[data-id="+user.userid+"]").closest("li").remove();
    }
}
var friend_util={
    friendTemplateHTML:"<li><h4>Username : <%=username%></h4>"+
        "<h4>Email : <%=email%></h4></li>"+
        '<a class="adduser" data-id="<%=id%>" data-name="<%=username%>">Add</a>',
    emptyHTML:"<li>...</li>",
    template:function(user){
        return _.template(friend_util.friendTemplateHTML)(user);
    },
    doFind:function(){
        $("ul#userlist").html("");
        var userinfo=$("#finduser").val();
        $.get("/api/find_user/"+userinfo,function(data){
            _.each(data,function(user){
                $("ul#userlist").append(friend_util.template(user));
            });
            $("ul#userlist").append(friend_util.emptyHTML);
        });
        
    },
    bind:function(){
        $("input#finduser").on("keypress",function(e){
            if(e.keyCode=="13"){
                friend_util.doFind();
            }
        });
        $("ul#userlist").click(function(e){
            var groupid=selected_data.groupid;
            if(!groupid){
                return ;
            }
            var $a=$(e.target).closest("a.adduser");
            if($a.length==1){
                var userid=$a.attr("data-id");
                var username=$a.attr("data-name");
                $.get("/api/group_add_member/"+groupid+"/"+userid,function(data){
                    if(data.fail){
                        console.log("add fail");
                    }else{
                        group_member_util.addRender({
                            userid:userid,
                            username:username
                        });
                    }
                });
            }
        });
    }
}
$(document).ready(function(){
    group_util.bind();
    friend_util.bind();
    group_member_util.bind();
});