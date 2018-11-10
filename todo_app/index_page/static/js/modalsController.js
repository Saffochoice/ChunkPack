$(function(){
  //modalsModule.openModal($('.add-chunk-modal__module'), 200);
  //modalsModule.closeModal($('.add-chunk-modal__module'), 200);
});
$('.create-chunk-icon__element.--main-header').click(function(){
  modalsModule.openModal($('.add-chunk-modal__module'), 200);
});
$('.close-button__element.--add-chunk-modal').click(function(){
  modalsModule.closeModal($('.add-chunk-modal__module'), 100);
});
$( document ).delegate('.modal-overlay__element', 'click', function(){
  modalsModule.closeModal($('.add-chunk-modal__module'), 100);
});
