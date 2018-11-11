$(function(){

});
$('.create-chunk-icon__element.--main-header').click(function(){
  modalsModule.openModal($('.typical-modal__module.--add-chunk'), 200);
});
$('.close-button__element').click(function(){
  modalsModule.closeModal($('.typical-modal__module'), 100);
});
$( document ).delegate('.modal-overlay__element', 'click', function(){
  modalsModule.closeModal($('.typical-modal__module'), 100);
});

// Single page
$('.edit__module.--single-chunk').click(function(){
  modalsModule.openModal($('.typical-modal__module.--edit-chunk'), 200);
});
