/* 确定性二维讲解；沿用共享影片引擎及其依据标记。 */
'use strict';
function heading(en, zh, a=1) {
  txt(en, 960, 220, {size:46, fam:F.disp, w:700, align:'center', c:C.white, a});
  txt(zh, 960, 275, {size:32, fam:F.zh, align:'center', c:C.dim, a});
}
function fivePath(y, left=1, loops=[2], a=1) {
  const xs=[380,670,960,1250,1540];
  for(let i=0;i<4;i++) {
    const col=i<2?C.cyan:C.mag;
    line(xs[i]+22,y,xs[i+1]-22,y,col,a,5);
    txt(String(i<2?left:1),(xs[i]+xs[i+1])/2,y-25,{size:32,align:'center',c:col,a});
  }
  xs.forEach((x,i)=>{
    ring(x,y,22,C.white,a,3);dot(x,y,18,'c',a);
    txt(String(i+1),x,y+64,{size:32,align:'center',c:C.white,a});
    if(loops.includes(i))ring(x,y-53,42,C.now,a,4);
  });
}
function spectrum(x,y,values,col,a=1) {
  line(x-290,y,x+290,y,C.dim,a,2);
  [-3,-2,-1,0,1,2,3].forEach(v=>{
    const xx=x+v*78;line(xx,y-6,xx,y+6,C.dim,a,2);
    txt(String(v),xx,y+36,{size:25,align:'center',c:C.dim,a});
  });
  values.forEach(v=>{ring(x+v*78,y,13,col,a,3);dot(x+v*78,y,24,'c',a);});
}
SCENES.question=S=>{
  badgeQ(S,[[0,null,'argued']]);
  heading('Which looped paths allow nSSP?','哪些带自环路径允许 nSSP？');
  fivePath(435,1,[2],1);
  panel(250,570,1420,205,1,C.argued,'EXISTENCE CRITERION');
  txt('even n: at least one loop',960,645,{size:38,fam:F.disp,align:'center',c:C.white});
  txt('odd n: a loop at an odd position',960,705,{size:38,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.7)});
  txt('Earlier full criterion: Carptopus, August 2026',960,800,{size:28,fam:F.disp,align:'center',c:C.dim,a:at(S,2,0.7)});
};
SCENES.test=S=>{
  badgeQ(S,[[0,null,'argued']]);
  heading('Two equations, only the zero solution','两个方程，只有零解');
  panel(220,330,710,400,1,C.cyan,'SUPPORT');
  panel(990,330,710,400,1,C.mag,'COMMUTATION');
  txt('A ∘ X = 0',575,465,{size:60,fam:F.math,align:'center',c:C.white});
  txt('X is zero on every arrow',575,560,{size:31,fam:F.disp,align:'center',c:C.cyan});
  txt('A Xᵀ = Xᵀ A',1345,465,{size:58,fam:F.math,align:'center',c:C.white});
  txt('Every real X is tested',1345,560,{size:33,fam:F.disp,align:'center',c:C.mag});
  txt('nSSP means: both equations force X = 0',960,795,{size:40,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.6)});
};
SCENES.split=S=>{
  badgeQ(S,[[0,null,'computed']]);
  const p=ease(at(S,2,1.8)),val=1+2*p;
  heading('Delete the center; compare the spectra','删去中心，比较两边的谱');
  panel(180,330,740,450,1,C.cyan,'LEFT BRANCH');
  panel(1000,330,740,450,1,C.mag,'RIGHT BRANCH');
  line(360,440,740,440,C.cyan,1,5);ring(360,440,19,C.white,1,3);ring(740,440,19,C.white,1,3);
  line(1180,440,1560,440,C.mag,1,5);ring(1180,440,19,C.white,1,3);ring(1560,440,19,C.white,1,3);
  txt(p<1?'1 → 3':'3',550,410,{size:38,align:'center',c:C.cyan});
  txt('1',1370,410,{size:38,align:'center',c:C.mag});
  spectrum(550,590,[-val,val],C.cyan);spectrum(1370,590,[-1,1],C.mag);
  txt(p<0.01?'same eigenvalues: failure':p<1?'separating the left spectrum':'{−3, 3} ∩ {−1, 1} = ∅ : success',960,805,{size:37,fam:F.math,align:'center',c:C.white});
};
SCENES.scale=S=>{
  badgeQ(S,[[0,null,'argued']]);
  heading('An even branch can be moved away from zero','偶支路的谱可以整体远离零');
  panel(230,330,1460,430,1,C.argued,'EXPLICIT INTEGER CHOICE');
  txt('even branch length d  →  weight M = d + 1',960,425,{size:43,fam:F.disp,align:'center',c:C.white});
  line(410,590,1510,590,C.dim,1,3);
  line(720,570,1200,570,C.mag,at(S,2,0.7),10);
  txt('−2',720,640,{size:36,fam:F.math,align:'center',c:C.white});
  txt('2',1200,640,{size:36,fam:F.math,align:'center',c:C.white});
  arrow(650,590,470,590,C.cyan,at(S,2,0.7),5);arrow(1270,590,1450,590,C.cyan,at(S,2,0.7),5);
  txt('scaled branch: |λ| > 2',580,710,{size:34,fam:F.math,align:'center',c:C.cyan});
  txt('unit branch: |λ| < 2',1340,710,{size:34,fam:F.math,align:'center',c:C.mag});
  txt('An empty branch has no eigenvalues to collide.',960,800,{size:32,fam:F.disp,align:'center',c:C.dim});
};
SCENES.recover=S=>{
  badgeQ(S,[[0,null,'argued']]);
  heading('Separate parities; recover every change','分离奇偶部分，恢复每个变化');
  panel(170,330,1580,190,1,C.cyan,'CONTINUANT');
  txt('Pₖ₊₂ = x Pₖ₊₁ − qₖ Pₖ',960,450,{size:58,fam:F.math,align:'center',c:C.white});
  panel(170,560,740,190,at(S,1,0.7),C.cyan,'EVEN POWERS');
  panel(1010,560,740,190,at(S,1,0.7),C.mag,'ODD POWERS');
  txt('1, x², x⁴, …',540,675,{size:46,fam:F.math,align:'center',c:C.cyan,a:at(S,1,0.7)});
  txt('x, x³, x⁵, …',1380,675,{size:46,fam:F.math,align:'center',c:C.mag,a:at(S,1,0.7)});
  txt('coprime branches → zero variations → X = 0',960,805,{size:39,fam:F.disp,align:'center',c:C.white,a:at(S,2,0.8)});
};
SCENES.enlarge=S=>{
  badgeQ(S,[[0,null,'argued']]);
  heading('Add small loops, then scale to integers','先添小自环，再缩放成整数');
  fivePath(435,3,at(S,0,1.4)>0.8?[0,2,4]:[2],1);
  txt('1/N',380,337,{size:31,fam:F.math,align:'center',c:C.now,a:at(S,0,1.4)});
  txt('1/N',1540,337,{size:31,fam:F.math,align:'center',c:C.now,a:at(S,0,1.4)});
  panel(270,590,1380,190,1,C.argued,'OPENNESS AND SCALING');
  txt('A₀ + D/N  →  N A₀ + D',960,710,{size:64,fam:F.math,align:'center',c:C.white,a:at(S,2,0.7)});
  txt('Full rank persists for sufficiently large N.',960,805,{size:36,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.8)});
};
SCENES.scope=S=>{
  badgeQ(S,[[0,null,'lean'],[1,null,'argued']]);
  heading('Exact scope, one construction','精确范围，同一构造');
  panel(180,330,1560,175,1,C.cyan,'EVEN-ORDER LEAN EXISTENCE');
  txt('positive even n  +  nonempty L',960,405,{size:43,fam:F.disp,align:'center',c:C.white});
  txt('exact support; every real test matrix X',960,465,{size:33,fam:F.disp,align:'center',c:C.dim});
  panel(180,555,1560,220,at(S,1,0.7),C.argued,'WRITTEN ARGUMENTS');
  txt('symmetric integers; odd order; spectral equivalence',960,635,{size:37,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.7)});
  txt('unit edges:  gcd(ℓ, n + 1) = 1',960,720,{size:45,fam:F.math,align:'center',c:C.white,a:at(S,2,0.7)});
  txt('Haobo Ma · Wenlin Zhang  |  Earlier criterion: Carptopus',960,805,{size:29,fam:F.disp,align:'center',c:C.dim});
};
FILM.poster=()=>{
  heading('Separate the branches, build the path','分开两条支路，构造一条路径');
  fivePath(450,3,[2],1);
  panel(240,620,1440,180,1,C.cyan,'FIVE POINTS · ONE LOOP');
  txt('{−3, 3} ∩ {−1, 1} = ∅',960,730,{size:68,fam:F.math,align:'center',c:C.white});
  txt('Haobo Ma · Wenlin Zhang | Earlier full criterion: Carptopus',960,860,{size:30,fam:F.disp,align:'center',c:C.dim});
};
