set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'tmhedberg/SimpylFold'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-syntastic/syntastic'
"Plugin 'nvie/vim-flake8'
Plugin 'ctrlpvim/ctrlp.vim'

" Key mapping
imap <C-e> <esc>$i<right>
imap <C-a> <esc>0i

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

"split navigations
set splitbelow
set splitright
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

" Pep8 indentation
au BufNewFile,BufRead *.py
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=120
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix

"Unnecessary Space
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

Plugin 'vim-scripts/indentpython.vim'
set encoding=utf-8
" Auto complete
Plugin 'ycm-core/YouCompleteMe'
Plugin 'davidhalter/jedi-vim'
"Some customization
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

let python_highlight_all=1
syntax on

" Ctrl+P settings
let g:ctrlp_working_path_mode = 'ra'
set wildignore+=*/tmp/*,*.so,*.swp,*.zip     " MacOSX/Linux
