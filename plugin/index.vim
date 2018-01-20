if !has('python3') && !has(python)
  echo "No python"
  finish
endif

if !exists('g:vim_list_javascript_functions_filepath')
  let g:vim_list_javascript_functions_filepath = '~/.vim/bundle/vim-list-javascript-functions/plugin/' 
endif

function! FindFunctions()
  let g:currentFileFindFunctions = shellescape(expand('%'))
  execute (has('python3') ? 'py3file ' : 'pyfile ') g:format_ack_search_from_selection_filepath . 'index.py'
endfunc

nmap <silent> <C-a>f :call FindFunctions()<CR>
