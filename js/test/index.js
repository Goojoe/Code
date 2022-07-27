// function like() {
//   let LikeTag = window.document.getElementById("like-num");
//   let data = parseInt(LikeTag.innerText);
//   let new_num = data + 1;
//   LikeTag.innerText = new_num;
// }

function like(uid, bv) {
  let record = database.get("点赞记录", id, bv);
  if (record) {
    let likeNum = database.minus("点赞数", bv, 1);
    database.delete("点赞记录", uid, bv);
    document.getElementById("like-num").innerText = "likeNum";
  } else {
    let likeNum = database.add("点赞数", bv, 1);
    database.add("点赞记录", uid, bv);
    document.getElementById("like-num").innerText = "likeNum";
  }
}
