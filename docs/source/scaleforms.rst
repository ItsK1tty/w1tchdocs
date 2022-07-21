
Decompiled Scaleforms
#########################

 frontend
=========

 AP_ICON
^^^^^^^^

* AP_ICON()

 CREW_TAG_MOVIECLIP
^^^^^^^^^^^^^^^^^^^

* CREW_TAG_MOVIECLIP()
* SET_CREW_TAG(crewTypeIsPrivate, crewTagContainsRockstar, crewTag, founderOrRank, crewColour)
* UNPACK_CREW_TAG(crewStr)
* debug()

 FEED_AWARD
^^^^^^^^^^^

* FEED_AWARD()
* INITIALISE(bgR, bgG, bgB, _flashAlpha, _flashRate, _bIsWideScreen, _bIsAsianLanguage, bgColor)
* SET_FEED_COMPONENT(awardName, txd, txn, xp, colourEnum, titleStr)
* hasPendingImage()
* CLEAR_TXD()

 FEED_CREW_RANKUP
^^^^^^^^^^^^^^^^^

* FEED_CREW_RANKUP()
* SET_FEED_COMPONENT(chTitle, chSubitle, chTXD, chTXN, bIsImportant)
* hasPendingImage()

 FEED_CREW_TAG
^^^^^^^^^^^^^^

* FEED_CREW_TAG()
* SET_FEED_COMPONENT(crewTypeIsPrivate, crewTagContainsRockstar, crewTag, rank, hasFounderStatus, bodyStr, isImportant, txd, imgStr, gamerStr, crewPackedStr)
* hasPendingImage()
* CLEAR_TXD()

 FEED_MESSAGE_TEXT
^^^^^^^^^^^^^^^^^^

* FEED_MESSAGE_TEXT()
* SET_FEED_COMPONENT(bodyStr, txd, txn, isImportant, iconEnum, nameStr, subtitleStr, crewPackedStr, icon2Enum, bTrimBody, iTextColor)
* hasPendingImage()
* flashOn()
* flashOff()
* CLEAR_TXD()
* getContentLength()

 FEED_REPLAY
^^^^^^^^^^^^

* FEED_REPLAY()
* INITIALISE(bgR, bgG, bgB, _flashAlpha, _flashRate, _bIsWideScreen, _bIsAsianLanguage, bgColor)
* SET_DISPLAY_CONFIG_OBJECT(dc)
* SET_FEED_COMPONENT(eType, sTitle, sSubtitle, iIcon, pctComplete, bFlash, sIcon)
* rotateSpinner(spinnerMC)
* pulseMC(bFadeOut, mc)
* lineToPtOnWheel(angle)
* onCleanup()

 FEED_STATS
^^^^^^^^^^^

* FEED_STATS()
* SET_FEED_COMPONENT(statTitleStr, statBodyStr, iconEnum, stepVal, barValue, isImportant, txd, txn)
* flashGlowOn(targetMC, blinkSpeed)
* flashGlowOff(targetMC, blinkSpeed)
* hasPendingImage()
* STREAM_COMP_READY()
* CLEAR_TXD()
* onCleanup()

 FEED_TICKER
^^^^^^^^^^^^

* FEED_TICKER()
* SET_FEED_COMPONENT(sBody, bIsImportant, bHasTokens, numIconFlashes)
* toggleIconVisibility(numFlashesLeft)

 FEED_TOOLTIPS
^^^^^^^^^^^^^^

* FEED_TOOLTIPS()
* INITIALISE(bgR, bgG, bgB, _flashAlpha, _flashRate, _bIsWideScreen, _bIsAsianLanguage, bgColor)
* SET_FEED_COMPONENT(bodyStr, isImportant)
* CLEAR_TXD()

 FEED_UNLOCK
^^^^^^^^^^^^

* FEED_UNLOCK()
* INITIALISE(bgR, bgG, bgB, _flashAlpha, _flashRate, _bIsWideScreen, _bIsAsianLanguage, bgColor)
* SET_FEED_COMPONENT(chTitle, chSubtitle, iIconType, bIsImportant, eTitleColour)
* flashOn()
* flashOff()

 FEED_VERSUS
^^^^^^^^^^^^

* FEED_VERSUS()
* INITIALISE(bgR, bgG, bgB, _flashAlpha, _flashRate, _bIsWideScreen, _bIsAsianLanguage, bgColor)
* SET_FEED_COMPONENT(ch1TXD, ch1TXN, val1, ch2TXD, ch2TXN, val2, vsStr, color1, color2)
* loadImg(sTXD, sTXN, imgMC)

 GAME_STREAM
^^^^^^^^^^^^

* GAME_STREAM()
* INITIALISE(mc)
* READY(id)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept, _isAsianLang)
* SET_HELPTEXT_HEIGHT(_helpTextHeight)
* adjustBaselines()
* SET_MINIMAP_VISIBLE_STATE(_mapVisibleState)
* SET_IMPORTANT_PARAMS(bgR, bgG, bgB, _flashAlpha, _flashRate)
* SET_NEXT_FEED_POST_BACKGROUND_COLOR(color)
* createStreamComponent(type, id)
* getStreamComponent(type, id)
* shuffleStreamComponents(currComp)
* animateInComplete(comp)
* reorderListComponents()
* deleteStreamComponent(type, id)
* deleteStreamComponentFromArray(bFromPending, type, id)
* removeFeedMC(ssObj)
* willComponentFit(compHeight, compID)
* validateComponent(ssObj)
* updatePendingItems()
* resetBgColor()
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID)
* SET_STREAM_COMPONENT()
* SNAP_NEXT_FEED_ITEM_INTO_POSITION()
* UPDATE_STREAM_COMPONENT()
* REMOVE_STREAM_COMPONENT(compTypeIndex, compType)
* UPDATE_STREAM_STATS()
* UPDATE_STREAM_TICKER()
* SHOW()
* HIDE()
* SHOW_CONTENT()
* ENABLE_SHOW_DEBUG_BOUNDS(isEnabled)
* repositionDebugLines()

 GAME_STREAM_ENUMS
^^^^^^^^^^^^^^^^^^

* GAME_STREAM_ENUMS()

 GTAV_ONLINE
^^^^^^^^^^^^

* GTAV_ONLINE()
* INITIALISE(mc)
* initScreenLayout(alignmentType)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SET_BIG_LOGO_VISIBLE(isBig, playFromStart)
* HIDE_ONLINE_LOGO()
* OVERRIDE_SIZE(scaleX, scaleY)
* OVERRIDE_POSITION(posX, posY)
* fadeLogoOut()
* SETUP_BIGFEED(bAlignRight)
* SETUP_TABS(count, bAlignRight)
* SET_BIGFEED_INFO(footerStr, bodyStr, whichTab, txd, txn, subtitle, urlDeprecated, title, newsItemType)
* SET_BIGFEED_BODY_TEXT(bodyStr)
* HIDE_BIGFEED_INFO()
* FADE_OUT_BIGFEED()
* FADE_IN_BIGFEED()
* SET_BIGFEED_PROGRESS(eHudColour, progress)
* END_BIGFEED()
* SET_BIGFEED_IMAGE(txd, image)
* SET_NEWS_CONTEXT(eContext)
* SET_TITLE()
* SET_DATA_SLOT(i)
* SET_DATA_SLOT_EMPTY()
* DISPLAY_VIEW(viewIndex, itemIndex)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* fadeImgIn()
* fadeImgOut()

 INSTRUCTIONAL_BUTTONS
^^^^^^^^^^^^^^^^^^^^^^

* INSTRUCTIONAL_BUTTONS()
* CONSTRUCTION_INNARDS()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept, _isAsian, _actualWidth, _actualHeight)
* TOGGLE_MOUSE_BUTTONS(hasButtons)
* saveSpinerFrame()
* SET_SAVING_TEXT(iconEnum, saveStr)
* REMOVE_SAVING()
* CLEAR_ALL()
* CLEAR_RENDER()
* OVERRIDE_POSITION(newX, newY, alignBottomRight)
* SET_CLEAR_SPACE(clearSpace)
* SET_LEADING(newLeading)
* SET_DATA_SLOT()
* SET_DATA_SLOT_EMPTY()
* CREATE_CONTAINER()
* CLEAR_BACKGROUNDS()
* DRAW_INSTRUCTIONAL_BUTTONS(layoutType)
* GET_NUMBER_OF_ROWS()
* createLineOfButtons(Xpos, startIndex)
* createItem(item)
* drawButton(mc, inputID)
* mouseEventProxy(_inputID)
* getWidth(obj, isString)
* createButtonIcon(buttonID, buttonParent, key)
* SET_BACKGROUND()
* processRollOver()
* processRollOut()
* generateTextField(textFieldName, textString, parentMovieClip)
* SET_PADDING(top, right, bottom, left)
* SET_BACKGROUND_COLOUR(r, g, b, a)
* OVERRIDE_RESPAWN_TEXT(id, txt)
* FLASH_BUTTON_BY_ID(buttonID, alpha, duration)
* removeButton(mc)
* SET_MAX_WIDTH(maxWidth)
* getFourThreeSafeZoneOffset(screenWidthPixels)
* requiresBackground()
* parse(incomingStr)
* addKey(instructions)
* addButton(instructions)
* isKey(str)
* parseForGamerName(TF, str)
* SET_HIT_AREA_VISIBLE(isVisible)
* debug()

 LANDING_PAGE
^^^^^^^^^^^^^

* LANDING_PAGE()
* debug()
* INITIALISE(mc)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, isWideScreen, _isHiDef, _isAsian)
* INIT_LANDING_PAGE()
* SET_BUTTON_SELECTED(buttonId)
* initButtons(dataArray)
* alignElements()

 LOADINGSCREEN_NEWGAME
^^^^^^^^^^^^^^^^^^^^^^

* LOADINGSCREEN_NEWGAME()
* INITIALISE(mc)
* SET_PROGRESS_BAR(percentage)
* SET_PROGRESS_TEXT(progressText)
* initProgressBar()
* initLogo()
* debug()
* getKeys()

 LOADINGSCREEN_STARTUP
^^^^^^^^^^^^^^^^^^^^^^

* LOADINGSCREEN_STARTUP()
* INITIALISE(mc)
* SET_SCREEN_ORDER(isSingleplayer)
* switchLoadSequence()
* SET_NEWS_SCREEN_ORDER(isSingleplayer)
* debug(id)
* randRange(min, max)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef)
* SET_CONTEXT(eContext)
* fadeLegals()
* removeLegals()
* fixJustifiedLegalText(tf, offset)
* getIsAmericanBuild()
* LEGAL(savingLabel, SocialClubLabel, loadingLabel, buildNumber, onlineVersionNumber)
* fadeAndRemoveMovieClip(fadeMc, fadeDuration)
* remove(Mc)
* removeRockstarSplash()
* INSTALL()
* SWITCH()
* prepLoadingScreens()
* SET_GTA_LOGO_VISIBLE(bVisible)
* switchToStaticGameLoadingScreens()
* TEST_BUTTONS(slot, icon, buttonText)
* TEST_INSTALL()
* updateButtonLayout()
* SET_BUTTONS(slot, icon, buttonText)
* setButtonText(buttonTF, buttonText)
* HIDE_BUTTONS()
* HIDE_PROGRESS_TEXT()
* SET_PROGRESS_TEXT(progressText)
* SET_PROGRESS_TITLE(progressTitle)
* initLogo()
* initButtons()
* initProgressBar()
* STARTUP_ANIMATED_LOADINGSCREENS()
* SHOW_NEXT_ANIMATED_LOADINGSCREEN()
* SHOW_NEXT_STATIC_LOADINGSCREEN()
* waitForLoadingScreen()
* texturesAreReadyAndAnimationIsDone()
* updateScreenIndex()
* updateNewsScreenIndex()
* getLoadingScreenObject(index)
* getLoadingScreenMovieClipName(index)
* loadTextures(textureDict)
* LOAD_TXD(textureDict, currScreenIndex)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* setupLoadscreen(textureDict, currScreenIndex)
* loadProgress(targetMC)
* loadInit(targetMC)
* setupLayers(loadscreenMc, loadscreenObject)
* playLoadscreen(loadscreenMc, loadscreenObject)
* loadscreenIsSettled(layer, duration, tweenargs, setup)
* exitLoadscreen(loadscreenMc, loadscreenObject)
* exitLoadscreenComplete()
* startTransition(duration)
* fadeInBlackOverlay(duration, onCompleteFunc)
* loadNextStaticScreen()
* onCompleteFadeToNews()
* removeLoadscreen(loadingScreenMc, loadingScreenObject)
* getNextLoadscreenObject()
* finishTransition()
* fadeOutBlackOverlay()
* createOverlay(parentMc)
* cleanUpTransition()

 MOUSE_EVENTS
^^^^^^^^^^^^^

* MOUSE_EVENTS()
* triggerEvent(params)

 MOUSE_POINTER
^^^^^^^^^^^^^^

* MOUSE_POINTER()
* INITIALISE(mc)
* SET_SCREEN_ASPECT(fPhysicalDifference, fLogicalDifference)

 ONLINE_POLICIES
^^^^^^^^^^^^^^^^

* ONLINE_POLICIES(mc)
* SET_SUBMIT_BUTTON(btnMc, btnText, rawText)
* SET_SUBMIT_BUTTON_ENABLED(btnMc, enable, isSelected)
* SET_TEXT_ENABLED_COLOR(tf)
* SET_TEXT_DISABLED_COLOR(tf)
* SET_HIGHLIGHT_COLOR(isSelected, clip, glowClip)
* SET_HIGHLIGHT_DISABLED_COLOR(clip, glowClip)
* SET_POLICY_TITLE(title, isRawText)
* SET_POLICY_INTRO(text, isRawText)
* SET_POLICY_TEXT(tos)
* SCROLL_POLICY_TEXT(scrollType)
* INIT_DOWNLOADED_POLICY()
* SET_POLICY_ACCEPTED_TEXT(text, isRawText)
* DISPLAY_DOWNLOADED_POLICY()
* DISPLAY_TOS()
* DISPLAY_EULA()
* DISPLAY_PP()
* SET_ONLINE_POLICY_TEXT(policy)
* SET_ONLINE_POLICY_TITLE(title)
* SET_ONLINE_POLICY_READ_TITLE(title)
* SET_ONLINE_POLICY_LINK_1(linkText)
* SET_ONLINE_POLICY_LINK_1_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_LINK_2(linkText)
* SET_ONLINE_POLICY_LINK_2_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_LINK_3(linkText)
* SET_ONLINE_POLICY_LINK_3_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_ACCEPT_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_ACCEPT_RADIO_BUTTON_STATE(state)
* SET_ONLINE_POLICY_ACCEPTED_TEXT(text)
* updatePolicyLinkLayout()
* SET_ONLINE_POLICY_SUBMIT_FIELD(text)
* SET_ONLINE_POLICY_SUBMIT_HIGHLIGHT(isEnabled, isSelected)
* DISPLAY_ONLINE_POLICY()
* INIT_DOWNLOADED_POLICY_UPDATE()
* SET_POLICY_UPDATE_TEXT(policy, isRawText)
* SET_POLICY_UPDATE_TITLE(title, isRawText)
* DISPLAY_POLICY_UPDATE()
* SHOW_PAGE_BY_ID(pageID)
* INIT_BUTTONS()
* DISPOSE_BUTTONS()
* INIT_TOS_BUTTONS()
* initTOSScrollButton(arrowMC, onClickEvent)
* onRollOverArrow(arrowMC)
* onRollOutArrow(arrowMC)
* disposeTOSScrollButton(arrowMC)
* onClickArrowUp()
* onClickArrowDown()
* SET_TEXT_HUDCOLOUR(tf, hudColourId)
* SET_MC_HUDCOLOUR(mc, hudColourId)
* GET_ROOT_DISPLAY_OBJECT()

 OPENING_CREDITS
^^^^^^^^^^^^^^^^

* OPENING_CREDITS(mc)
* INITIALISE(mc)
* TEST_LOGO(fadeInDuration, fadeOutDuration, logoFadeInDuration, logoFadeOutDuration, logoFadeInDelay, logoFadeOutDelay, logoScaleDuration)
* TEST_CREDIT_BLOCK(role, names, align, xOffset, namesXOffset, stepDuration, animInStyle, animInValue, animOutValue)
* TEST_SINGLE_LINE(animInStyle, animInValue, animOutValue)
* SETUP_SINGLE_LINE(mcName, fadeInDuration, fadeOutDuration, x, y, align)
* ADD_TEXT_TO_SINGLE_LINE(mcName, text, font, colour, isRawText, language, yOffset)
* SHOW_SINGLE_LINE(mcName, animInStyle, animInValue)
* SETUP_CREDIT_BLOCK(mcName, x, y, align, fadeInDuration, fadeOutDuration)
* ADD_ROLE_TO_CREDIT_BLOCK(mcName, role, xOffset, colour, isRawText, language)
* ADD_NAMES_TO_CREDIT_BLOCK(mcName, names, xOffset, delimiter, isRawText)
* SHOW_CREDIT_BLOCK(mcName, stepDuration, animInStyle, animInValue)
* SHOW_LOGO(mcName, fadeInDuration, fadeOutDuration, logoFadeInDuration, logoFadeOutDuration, logoFadeInDelay, logoFadeOutDelay, logoScaleDuration)
* unhideLogo(mcName)
* HIDE_LOGO(mcToHide)
* HIDE(mcToHide, stepDuration, animOutStyle, animOutValue)
* REMOVE(mcToRemove)
* REMOVE_MC(mcToRemove)
* REMOVE_ALL()
* createOverlay(parentMc, depth)
* getMovieClipFromName(mcName)
* normaliseXRightAlignment(mcName)
* setAlignment(align)
* getAnimInStyle(animStyle)
* getColour(col)
* getObjectFromMcName(mcName)
* stringInArray(input, what)

 PAUSE_MENU_BAR
^^^^^^^^^^^^^^^

* PAUSE_MENU_BAR()
* INITIALISE(mc)
* BUILD_MENU(params)
* createArrowMouseCatcher(x, y, w, h, mPress)
* removeArrowMouseCatcher(arrowCatcherMC)
* onLeftArrowClick()
* onRightArrowClick()
* LOCK_MOUSE_SUPPORT(_mClickOn, _mRollOverOn)
* IS_CHAR_SELECT(_charSelectOn)
* REMOVE_MENU()
* SET_ALL_HIGHLIGHTS(hOn, colourID)
* SET_MENU_HEADER_TEXT_BY_INDEX(menuIndex, label, widthSpan)
* SET_MENU_ITEM_ALERT(menuindex, warnStr, col)
* SET_MENU_COLOUR(menuindex, colourEnum)
* LOCK_MENU_ITEM(menuindex, isLocked)
* SCROLL_MENU_IN_DIR(params)
* ROLLOVER_MENU(bool)
* HIGHLIGHT_MENU(index)
* getMenuWidth(items)
* scrollMenu(x, duration, easetype)
* SET_HEADER_ARROWS_VISIBLE(isLeftArrowVisible, isRightArrowVisible)
* SET_CODE_MENU_INDEX(rollOverIndex)
* SET_CODE_MENU_SELECT()

 PAUSE_MENU_CALIBRATION
^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CALIBRATION()
* INITIALISE(mc)
* SET_ARROW_ALPHA(arrowID, a)
* SET_BUTTONS()
* onMouseEvent(evtType, targetMC, args)

 PAUSE_MENU_CONFIGURATION_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CONFIGURATION_LIST()
* INITIALISE(mc)
* SET_HIGHLIGHT(i)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_TITLE(str1, str2, str3)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_FOCUS(isFocused)
* SET_KEY_CONFIG_COLUMN(colIndex)
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_FREE_MODE
^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_FREE_MODE()
* INITIALISE(mc)
* DISPLAY_VIEW(viewIndex, itemIndex)
* setColumnDependent(columnMC)
* setIsLastItem()
* setCharCreatorItem()
* SET_STATE(i, mc)
* SET_HIGHLIGHT(i)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_TITLE(titleStr, desc, pagination)
* flashHelpIn()
* flashHelpOut()
* SET_DESCRIPTION(helpStr, flashIcon, flashHelp)
* INIT_SCROLL_BAR(visible, columns, scrollType, arrowPosition, override, xColOffset)
* SET_SCROLL_BAR(currentPosition, maxPosition, maxVisible, caption)
* getHelpY()
* setLinkedMCPos(yOrigin)
* SET_FOCUS(isFocused)
* getVisibleHeight()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_FREEMODE_DETAILS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_FREEMODE_DETAILS()
* INITIALISE(mc)
* setImageLoaderInfo(_gfxName, _depth)
* SET_TITLE(str)
* transitionInBitmap()
* transitionComplete()
* ON_DESTROY()
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)
* updateDescBG()
* SET_FOCUS(isFocused)
* getKeys()
* SET_INPUT_EVENT(direction)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)

 PAUSE_MENU_HEADER
^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_HEADER()
* INITIALISE(mc)
* SHOW_DEBUG(b)
* dbg(Str)
* LOCK_MOUSE_SUPPORT(_mClickOn, _mRollOverOn)
* IS_CHAR_SELECT(_charSelectOn)
* SET_TEXT_SIZE(isAsian, sizeOverride)
* shrinkAsianDetails()
* SET_HEADER_TITLE(title, verified, description, isChallenge)
* SHIFT_CORONA_DESC(shiftDesc, hideTabs)
* setDescWidth()
* SET_HEADING_DETAILS(str1, str2, str3, isSingleplayer)
* SHOW_HEADING_DETAILS(bool)
* SET_CREW_TAG(crewTypeIsPrivate, crewTagContainsRockstar, crewTag, founderOrRank)
* SET_HEADER_BG_IMG(txd, bgTexturePath, xPos)
* loadedBgImg()
* SET_CREW_IMG(txd, crewTexturePath, show)
* loadedCrewImg()
* SET_CHAR_IMG(txd, charTexturePath, show)
* loadedCharImg()
* adjustHeaderPositions()
* BUILD_MENU()
* REMOVE_MENU(clearForRestart)
* CLEAR_TXDS()
* SET_MENU_HEADER_TEXT_BY_INDEX(menuIndex, label, widthSpan, forceUpper)
* WEIGHT_MENU()
* SET_MENU_ITEM_COLOUR(menuindex, colourEnum)
* LOCK_MENU_ITEM(menuindex, isLocked)
* SET_MENU_ITEM_ALERT(menuindex, warnStr, col)
* SCROLL_MENU_IN_DIR(dir)
* HIGHLIGHT_MENU(index)
* SET_ALL_HIGHLIGHTS(allHighlights, _colourID)
* SHOW_MENU(bool)
* ADD_TXD_REF_RESPONSE(txd, strRef, success)
* TXD_HAS_LOADED(txd, success, strRef)
* TXD_ALREADY_LOADED(txd, strRef)

 PAUSE_MENU_INSTRUCTIONAL_BUTTONS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_INSTRUCTIONAL_BUTTONS()
* SET_PADDING(_padding)
* INITIALISE(mc)

 PAUSE_MENU_KEYMAP_CATEGORY
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_KEYMAP_CATEGORY()
* INITIALISE(mc)
* DISPLAY_VIEW(viewIndex, itemIndex)
* setColumnDependent(columnMC)
* SET_HIGHLIGHT(i)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_DESCRIPTION(helpStr, flashHelp)
* INIT_SCROLL_BAR(visible, columns, scrollType, arrowPosition, override, xColOffset)
* SET_SCROLL_BAR(currentPosition, maxPosition, maxVisible, caption)
* getHelpY()
* setLinkedMCPos(yOrigin)
* SET_FOCUS(isFocused)
* getVisibleHeight()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_PAGES_KEYMAP
^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_KEYMAP()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_SETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_SETTINGS()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_SETTINGS
^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_SETTINGS()
* INITIALISE(mc)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_CONTROL_IMAGE(textureDictionary, textureName)
* SET_CONTROL_LABELS()
* SET_VIDEO_MEMORY_BAR(initialise, textlabel, percent, colour)
* setControlsText(tf, str)
* SET_TITLE(title)
* setSpeaker(strID, col, a)
* createTexture(txD, txN, txX, txY, txW, txH)
* textureLoaded()
* SET_DESCRIPTION(description, txD, txN, txX, txY, txW, txH)
* ON_DESTROY()
* resetVisibleItems()
* SET_STATE(i)
* SET_FOCUS(isFocused)
* SET_INPUT_EVENT(direction)
* SET_HIGHLIGHT(i)

 PAUSE_MENU_SP_CONTENT
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_SP_CONTENT()
* INITIALISE(mc)
* SET_MENU_LEVEL(_menuLevel)
* DEBUG_ALL()
* SHOW_DEBUG(b)
* dbgColVisible()
* dbgColDebug()
* dbgColLeft()
* dbgColRight()
* localLoad()
* DEBUG_INIT_MOUSE_EVENTS()
* INIT_MOUSE_EVENTS()
* SET_TEXT_SIZE(isAsian, sizeOverride)
* INSTRUCTIONAL_BUTTONS(func)
* LOCK_MOUSE_SUPPORT(_mClickOn, _mRollOverOn)
* INIT_M_AUX()
* DELTA_MOUSE_WHEEL(delta)
* MOUSE_COLUMN_SHIFT(_mScrollType)
* PRESS_SHIFT_DEPTH(dir)
* M_OVER_EVENT(index, colID, pmb)
* M_OUT_EVENT(index, colID)
* M_PRESS_EVENT(index, colID, advance, bIgnoreStateChange)
* FILTER_M_EVENT(index, colID, action, advance, pmb, bIgnoreStateChange)
* CLICK_PAUSE_MENU_ITEM(index, colID)
* CLICK_SCROLL_COLUMN_ARROW(scrollDirEnum, colID)
* CLEAR_ALL_HOVER()
* BLOCK_HEADER_ADVANCE(b)
* BUILD_MENU()
* BUILD_MENU_GFX_FILES()
* SET_HEADER_TITLE()
* SET_HEADING_DETAILS()
* SET_MENU_HEADER_TEXT_BY_INDEX()
* SET_MENU_ITEM_COLOUR()
* SET_CHAR_IMG()
* SET_CREW_IMG()
* SET_CREW_TAG()
* SCROLL_MENU_IN_DIR()
* HIGHLIGHT_MENU()
* LOCK_MENU_ITEM()
* SET_CONTENT_SCALED(isScaled, tlx, tly, brx, bry)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen)
* SET_INPUT_EVENT(inputID)
* SET_COLUMN_INPUT_EVENT()
* GET_COLUMN_SELECTION()
* SET_COLUMN_TITLE()
* SET_DESCRIPTION()
* SET_COLUMN_FOCUS()
* SET_COLUMN_HIGHLIGHT()
* INIT_COLUMN_SCROLL()
* SET_COLUMN_SCROLL()
* SET_COLUMN_CAN_JUMP()
* ALLOW_CLICK_FROM_COLUMN()
* SET_DATA_SLOT()
* UPDATE_SLOT()
* ADD_SLOT()
* DISPLAY_DATA_SLOT()
* SET_DATA_SLOT_EMPTY()
* SHOW_COLUMN()
* SHOW_AND_CLEAR_COLUMNS()
* KILL_PAGE()
* SHOW_CONTEXT_MENU(bool)
* SET_CONTEXT_SLOT()
* SET_CONTEXT_EMPTY()
* DISPLAY_CONTEXT_SLOT()
* SHOW_WARNING_MESSAGE(bShow, columnIndex, numCols, bodyStr, titleStr, bgHeight, txd, txn, imgAlignment, footerStr, bRequestTXD)
* removeErrorImgMC()
* setIsNavigatingContent(bIsNavigatingContent)
* SET_SC_LOGGED(logged)
* SET_CONTROL_LABELS()
* SET_CONTROL_IMAGE()
* SET_VIDEO_MEMORY_BAR()
* SET_DISPLAY_MICS()
* SET_PLAYERLIST_ICON()
* MENU_STATE(id)
* LOAD_CHILD_PAGE(gfxFilePath, _menustate, inceptDir)
* LOADED_PAGE()
* PAGE_FADE_IN()
* MENU_SECTION_JUMP(mindex, loadContent, scriptLayoutChange)
* FRONTEND_CONTEXT_PRESS()
* MENU_KEY_PRESS_ACTIONS(dir)
* MENU_STATE_LOAD(oldMenuState)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* onWarningImgLoaded()

 PAUSE_MENU_TEXT_LIST_DOUBLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_TEXT_LIST_DOUBLE()
* INITIALISE(mc)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_FOCUS(isFocused)
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_VERTICAL_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_VERTICAL_LIST()
* INITIALISE(mc)
* SET_HIGHLIGHT(i)
* SET_INPUT_EVENT(direction)

 PAUSE_MP_MENU_FRIENDS_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MP_MENU_FRIENDS_LIST()
* INITIALISE(mc)
* UPDATE_SLOT(_viewIndex, _slotIndex)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* parseIcons(args)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DESCRIPTION(joiningStr, yPos)
* SET_HIGHLIGHT(i)
* SET_INPUT_EVENT(direction)
* ON_DESTROY()

 PAUSE_MP_MENU_PLAYER_MODEL
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MP_MENU_PLAYER_MODEL()
* INITIALISE(mc)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_TITLE(str)
* ADD_TXD_REF(txd, txn)
* ON_DESTROY()
* SET_INPUT_EVENT(direction)

 POPUP_WARNING
^^^^^^^^^^^^^^

* POPUP_WARNING()
* INITIALISE(mc)
* debug()
* SHOW_POPUP_WARNING(msecs, titleMsg, warningMsg, promptMsg, showBg, alertType, errorMsg)
* HIDE_POPUP_WARNING(msecs)
* SET_LIST_ROW(index, name, cash, rp, lvl, colour)
* SET_LIST_ITEMS(highlightIndex)
* REMOVE_LIST_ITEMS()
* repositionListY()
* repositionListGroup()
* SET_LIST_HIGHLIGHT(highlightIndex)
* SET_ALERT_IMAGE(txd, texture)
* SET_ALERT_IMAGE_WITH_GANG_HIGHLIGHT(txd, texture, gangEnum, r, g, b)
* loadTextureIntoMovieClip(txd, texture, targetLoadedInto)

 ROCKSTAR_VERIFIED
^^^^^^^^^^^^^^^^^^

* ROCKSTAR_VERIFIED()
* SET_VERIFIED(type, colourEnum)

 RP_ICON
^^^^^^^^

* RP_ICON()

 SOCIAL_CLUB2
^^^^^^^^^^^^^

* SOCIAL_CLUB2(mc)
* RESET_MENU()
* CREATE_BLIP_LAYER(page, xPos, yPos)
* SET_HIGHLIGHT_COLOR(isSelected, clip, glowClip)
* SET_HIGHLIGHT_DISABLED_COLOR(clip, glowClip)
* SET_TEXT_ENABLED_COLOR(tf)
* SET_TEXT_DISABLED_COLOR(tf)
* SET_TEXT_HUDCOLOUR(tf, hudColourId)
* SET_MC_HUDCOLOUR(mc, hudColourId)
* SET_SUBMIT_BUTTON(btnMc, btnText, rawText)
* SET_SUBMIT_BUTTON_ENABLED(btnMc, enable, isSelected)
* SET_GAMERNAME(gamerName)
* SET_SOCIAL_CLUB_PRESENCE(scPresence)
* SET_SOCIAL_CLUB_PRESENCE_ACTIVE(scPresence)
* SET_NEWS_TEXT(heading, title, newsItem)
* SET_SOCIAL_CLUB_NAME()
* SET_WELCOME_TITLE_TEXT(title)
* SET_WELCOME_INTRO_TEXT(intro)
* SET_WELCOME_CALLOUT_TEXT(callout)
* SET_WELCOME_IMAGE(txd, image)
* SET_WELCOME_FALLBACK_IMAGE_VISIBILITY(visible)
* ADD_TXD_REF_RESPONSE(txd)
* SET_WELCOME_JOIN_HIGHLIGHT(isSelected)
* SET_WELCOME_SIGN_IN_HIGHLIGHT(isSelected)
* SETUP_WELCOME_TABS(count)
* SET_WELCOME_TAB(whichTab)
* DISPLAY_WELCOME_PAGE()
* SET_ONLINE_POLICY_TEXT(policy)
* SET_ONLINE_POLICY_TITLE(title)
* SET_ONLINE_POLICY_READ_TITLE(title)
* SET_ONLINE_POLICY_LINK_1(linkText)
* SET_ONLINE_POLICY_LINK_1_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_LINK_2(linkText)
* SET_ONLINE_POLICY_LINK_2_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_LINK_3(linkText)
* SET_ONLINE_POLICY_LINK_3_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_ACCEPT_HIGHLIGHT(isSelected)
* SET_ONLINE_POLICY_ACCEPT_RADIO_BUTTON_STATE(state)
* SET_ONLINE_POLICY_ACCEPTED_TEXT(text)
* updatePolicyLinkLayout()
* SET_ONLINE_POLICY_SUBMIT_FIELD(text)
* SET_ONLINE_POLICY_SUBMIT_HIGHLIGHT(isEnabled, isSelected)
* DISPLAY_ONLINE_POLICY()
* SET_POLICY_TITLE(title)
* SET_POLICY_TEXT(tos)
* SCROLL_POLICY_TEXT(scrollType)
* INIT_DOWNLOADED_POLICY()
* DISPLAY_DOWNLOADED_POLICY()
* SET_EMAIL_ADDRESS(emailAddress)
* SET_NICKNAME(nickname)
* SET_SIGN_UP_TITLE(title)
* SET_SIGN_UP_TEXT(text)
* SET_SIGN_UP_NICKNAME_HIGHLIGHT(isSelected)
* SET_SIGN_UP_EMAIL_ADDRESS_HIGHLIGHT(isSelected)
* SET_SIGN_UP_PASSWORD_HIGHLIGHT(isSelected)
* SET_SIGN_UP_PASSWORD(password)
* SET_SIGN_UP_RADIO_BUTTON_STATE(state)
* SET_HIGLIGHT_INPUT_MAILING_LIST(isSelected)
* SET_INPUT_MAILING_LIST(text)
* SET_SIGN_UP_SUBMIT_TEXT(text)
* SET_SIGN_UP_SUBMIT_HIGHLIGHT(isSelected)
* SET_SIGN_UP_SUBMIT_DISABLED()
* SET_SIGN_UP_NICKNAME_STATE(message, icon)
* SET_SIGN_UP_EMAIL_STATE(message, icon)
* SET_SIGN_UP_PASSWORD_STATE(message, icon)
* DISPLAY_SIGN_UP()
* INIT_SIGN_UP()
* SET_SIGN_IN_TITLE(title)
* SET_SIGN_IN_TEXT(text)
* SET_SIGN_IN_EMAIL_ADDRESS_HIGHLIGHT(isSelected)
* SET_SIGN_IN_PASSWORD_HIGHLIGHT(isSelected)
* SET_SIGN_IN_PASSWORD(password)
* SET_SIGN_IN_SUBMIT_DISABLED()
* SET_SIGN_IN_SUBMIT_HIGHLIGHT(isSelected)
* SET_SIGN_IN_EMAIL_STATE(message, icon)
* SET_SIGN_IN_PASSWORD_STATE(message, icon)
* SET_SIGN_IN_PASSWORD_RESET_TEXT(text)
* SET_SIGN_IN_PASSWORD_RESET_HIGHLIGHT(isSelected)
* INIT_SIGN_IN()
* DISPLAY_SIGN_IN()
* DISPLAY_SYNC(scTitle, scText, showSpinner)
* SET_DOB_SIGNUP_TITLE(title)
* SET_DOB_SIGNUP_TEXT(text)
* SET_DOB_HIGHLIGHT(isSelected, whichDOB)
* SET_DOB_TEXT(whichDOB, str)
* RESET_DOB_TEXT(whichDOB)
* SET_DOB_ERROR(errorMessage)
* SET_DOB_SUBMIT_HIGHLIGHT(isSelected)
* SET_DOB_SUBMIT_DISABLED()
* DISPLAY_DOB_PAGE()
* SET_CONFIRM_TITLE(title)
* SET_CONFIRM_TEXT(text)
* SET_CONFIRM_TEXT_BLIPS(label)
* SET_CONFIRM_EMAIL_LABEL_TEXT(text)
* SET_CONFIRM_USER_EMAIL_TEXT(text)
* SET_CONFIRM_NICKNAME_LABEL_TEXT(text)
* SET_CONFIRM_USER_NICKNAME_TEXT(text)
* SET_CONFIRM_NEWSLETTER_TEXT(text)
* DISPLAY_CONFIRM_PAGE()
* SET_SIGN_IN_DONE_TITLE(title)
* SET_SIGN_IN_DONE_TEXT(text)
* DISPLAY_SIGN_IN_DONE_PAGE()
* SET_SIGN_UP_DONE_TITLE(title)
* SET_SIGN_UP_DONE_TEXT(text)
* DISPLAY_SIGN_UP_DONE_PAGE()
* SET_FORGOT_PASSWORD_TITLE(title)
* SET_FORGOT_PASSWORD_TEXT(text)
* SET_FORGOT_PASSWORD_EMAIL_STATE(message, icon)
* SET_FORGOT_PASSWORD_EMAIL_HIGHLIGHT(isSelected)
* SET_FORGOT_PASSWORD_SUBMIT_HIGHLIGHT(isSelected)
* DISABLE_FORGOT_PASSWORD_SUBMIT_HIGHLIGHT()
* INIT_FORGOT_PASSWORD_PAGE()
* DISPLAY_FORGOT_PASSWORD_PAGE()
* SET_FORGOT_PASSWORD_DONE_TITLE(title)
* SET_FORGOT_PASSWORD_DONE_TEXT(text)
* DISPLAY_FORGOT_PASSWORD_DONE_PAGE()
* SET_ERROR_TITLE(title)
* SET_ERROR_TEXT(text)
* SET_ERROR_BUTTON_TEXT(text)
* DISPLAY_ERROR_PAGE()
* SHOW_PAGE_BY_ID(pageID)
* INIT_ONLINE_POLICY_BUTTONS()
* INIT_TOS_BUTTONS()
* initTOSScrollButton(arrowMC, onClickEvent)
* onRollOverArrow(arrowMC)
* onRollOutArrow(arrowMC)
* disposeTOSScrollButton(arrowMC)
* onClickArrowUp()
* onClickArrowDown()
* INIT_SID_BUTTONS()
* onSubmitBtnMouseEvent(evtType, targetMC)
* DISPOSE_BUTTONS()
* GET_ROOT_DISPLAY_OBJECT()

 generic
========

 AIRCRAFT_DIALS
^^^^^^^^^^^^^^^

* AIRCRAFT_DIALS()
* INITIALISE(mc)
* SET_DASHBOARD_DIALS(fuel, temp, oilPressure, battery, fuelPSI, airSpeed, verticleAirSpeed, compass, roll, pitch, alt_small, alt_large)
* SET_DASHBOARD_LIGHTS(gearUp, gearDown, breach)
* SET_AIRCRAFT_HUD(airTXT, fuelTXT, oilTXT, vacuumTXT)
* getDialAngle(minRot, maxRot, scale, isClockwise)
* percFromRad(input)
* debug()

 AMBIENT_CLIP
^^^^^^^^^^^^^

* AMBIENT_CLIP()
* SET_TEXT_WITH_WIDTH(str, bgWidth, showFadeOut)
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 AMMO_MASTER
^^^^^^^^^^^^


 APP_JOB_LIST
^^^^^^^^^^^^^

* APP_JOB_LIST()
* INITIALISE(mc)
* construct()
* populateContent()
* setState(item, isActive)
* parseForGamerName(TF, str)

 APP_MISSION_STATS_VIEW
^^^^^^^^^^^^^^^^^^^^^^^

* APP_MISSION_STATS_VIEW()
* INITIALISE(mc)
* construct()
* populateContent()
* CLEAN_UP_DATA()

 APP_NUMBERPAD
^^^^^^^^^^^^^^

* APP_NUMBERPAD()
* INITIALISE(mc)
* construct(_dataProviderUI)
* renderContainers()
* populateContent(_dataProviderUI)
* navigate(direction)
* GET_CURRENT_SELECTION()
* setState(item, isActive)

 APP_SECUROSERV_HACKING
^^^^^^^^^^^^^^^^^^^^^^^

* APP_SECUROSERV_HACKING()
* INITIALISE(mc)
* APP_FUNCTION()
* CLOSE_APP()
* CLEAN_UP_DATA()
* construct()
* populateContent()
* initNoSignal()
* initWeakSignal()
* initHacking(percentage)
* initComplete()
* initProgress()
* initMessage(label, isLiteral)
* flashMessage()

 APP_TODO_LIST
^^^^^^^^^^^^^^

* APP_TODO_LIST()
* INITIALISE(mc)
* construct()
* populateContent()
* setState(item, isActive)

 APP_TODO_VIEW
^^^^^^^^^^^^^^

* APP_TODO_VIEW()
* INITIALISE(mc)
* construct()
* populateContent()
* CLEAN_UP_DATA()

 APP_TRACKIFY
^^^^^^^^^^^^^

* APP_TRACKIFY()
* INITIALISE(mc)
* setTargetByID(targetID, direction, distance, range, relativeDepth, heightIndicator)
* checkRangeForAllTargets()
* displayDepth(relativeDepth)
* showDepth(_vis)
* construct(dataProviderUI)
* populateContent(dataProviderUI)
* APP_FUNCTION()
* setupMainScreen()
* setupMainScreenSkipLoading()
* updateTargetPositionNew(newTarget)
* testAllTargets()
* set_loading_text(textString)
* flashOn()
* flashOff(mc)
* animateSweep()
* CLEAN_UP_DATA()
* CLOSE_APP()
* checkAndRemoveTween(mc)
* showHackingAppState(buttonLabel, isActive)
* checkAndSetText(TF, textLabel)

 ARCADE_BUSINESS_HUB
^^^^^^^^^^^^^^^^^^^^

* ARCADE_BUSINESS_HUB()
* initialise(mc)
* SET_PLAYER(gamerName, mugshot)
* ADD_BUSINESS(id, title, texture, statLabel1, normStatLevel1, statLabel2, normStatLevel2, canResupply, isLocked)
* getBusiness(id)
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* SHOW_SPECIAL_CARGO_OVERLAY(title, message, button1Label, button2Label, button3Label, button4Label, button5Label)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)

 ARCADE_MANAGEMENT
^^^^^^^^^^^^^^^^^^

* ARCADE_MANAGEMENT()
* initialise(mc)
* SET_PLAYER_DATA(gamername, mugshot, location, arcadeTexture, totalEarnings)
* ADD_CABINET(id, name, description, texture, price, salePrice, owned)
* getCabinet(id)
* ADD_UPGRADE(id, title, description, texture, price, salePrice, owned)
* getUpgrade(id)
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* IS_HISTORY_EMPTY()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* updateButtons()
* setArcadeImageVisibility(isVisible)
* setArcadeImageScrollPosition(y)
* TXD_HAS_LOADED(txd, success, id)
* setSelectedCabinet(cabinetID)

 ARENA_CAREER_WALL
^^^^^^^^^^^^^^^^^^

* ARENA_CAREER_WALL()
* initialise(mc)
* SET_STATS(gamername, rank, totalArenaPoints, noLongerUsed1, arenaPoints, currTier, currTierProgress, gamesPlayed, wins, losses, kills, deaths, spectatorKills, favouriteVehicle, noLongerUsed2, bestMode, worstMode)
* SET_TEXTURES(textureDictionary, note1, note2, note3)
* SHOW_SCREEN(screenID)
* SHOW_UNLOCK(id)
* HIDE_UNLOCK(id)
* showScreen(screenID)
* TXD_HAS_LOADED(txd, success, id)

 ARENA_GUN_CAM
^^^^^^^^^^^^^^

* ARENA_GUN_CAM()
* INITIALISE(mc)
* SET_WEAPON_TYPE(weaponType)
* SET_WEAPON_VALUES(machineGunVal, missileVal, pilotMissileVal)
* SET_ZOOM_VISIBLE(isVisible)

 ARROW_WITH_EVENTS
^^^^^^^^^^^^^^^^^^

* ARROW_WITH_EVENTS()
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 ATM
^^^^

* ATM()
* INITIALISE(mc)
* GET_CURRENT_SELECTION()
* SET_DATA_SLOT_EMPTY()
* SET_DATA_SLOT(slotID)
* SET_INPUT_EVENT(direction)
* SET_INPUT_SELECT()
* SET_ANALOG_STICK_INPUT(isLeftStick, mouseX, mouseY)
* SET_BROWSER_CURSOR_SPEED_MODIFIER(newSpeed)
* SET_CURSOR_STATE(cursorState)
* GET_CURSOR_STATE()
* SHOW_CURSOR(visible)
* SET_MOUSE_INPUT(mouseX, mouseY)
* setCursorBusy()
* setCursorInvisible()
* getCurrentSelectionFromCursorPosition()
* DISPLAY_BALANCE(_playerName, _balanceString, _balance)
* DISPLAY_TRANSACTIONS()
* DISPLAY_MESSAGE()
* DISPLAY_CASH_OPTIONS()
* DISPLAY_MENU()
* setupView(viewMC)
* enterPINanim()
* pinBeep()
* update()
* formatAmount(value)
* updateBalance()
* SCROLL_PAGE(amount)
* navigate(direction)
* setState(item, isActive)
* UPDATE_TEXT()

 AUDIO_CLIP
^^^^^^^^^^^

* AUDIO_CLIP()
* SET_TEXT_WITH_WIDTH(str, bgWidth, showFadeOut)
* SET_ANIMATED_ICON_VISIBLE(isVisible)
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 BANK_JOB_LOGIN
^^^^^^^^^^^^^^^

* BANK_JOB_LOGIN()
* initialise(mc)

 BIKER_BUSINESSES
^^^^^^^^^^^^^^^^^

* BIKER_BUSINESSES()
* initialise(mc)
* ACTIVATE()
* DEACTIVATE()
* SET_PLAYER_DATA(userName, isAdmin)
* ADD_BUSINESS(id, type, txd, location, description, status, price, salePrice, stockLevel, stockValue, suppliesLevel, canResupply, totalSales, timesRaided, successfulSales, resupplyButtonEnabled, resupplyCost, resupplySaleCost, isInStarterPack)
* ADD_BUSINESS_STATS(id, resupplySuccess, sellSuccessLS, sellSuccessBC, ceasedSupplies, ceasedCapacity)
* ADD_BUSINESS_UPGRADE(id, index, description, price, txd, salePrice)
* REMOVE_BUSINESS_UPGRADE(id, index)
* SET_BUSINESS_UPGRADE_STATUS(id, index, isEnabled)
* ADD_BUSINESS_BUYER(id, index, buyerName, amount, price)
* REMOVE_BUSINESS_BUYER(id, index)
* SET_BUSINESS_BUYER_STATUS(id, index, isEnabled)
* SET_START_PRODUCTION_STATUS(isEnabled)
* SHOW_OVERLAY(messageLabel, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* SHOW_HOMEPAGE()
* GET_SELECTED_BUSINESS_ID()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* getBusinessByID(id)
* quit()
* TXD_HAS_LOADED(txd, success, id)

 BIKER_MISSION_WALL
^^^^^^^^^^^^^^^^^^^

* BIKER_MISSION_WALL()
* initialise(mc)
* SET_MISSION(index, title, description, txd, x, y)
* SET_STAT(index, description, stat)
* SET_SELECTED_MISSION(index)
* HIDE_MISSION(index)
* setMapMarker(x, y, index)
* addImage(txd, id, imageTextField)
* textureLoaded(txd)
* clearImageQueue()
* displayImage(txd, id, imageTextField)
* TXD_HAS_LOADED(txd, success, id)
* dispose()
* setLocalisedText(tf, label)

 BINOCULARS
^^^^^^^^^^^

* BINOCULARS()
* INITIALISE(mc)
* initScreenLayout()

 BLIMP_TEXT
^^^^^^^^^^^

* BLIMP_TEXT()
* initialise(mc)
* SET_SCROLL_SPEED(scrollSpeed)
* SET_COLOUR(colour)
* SET_MESSAGE(message)
* startScroll(goalX, duration)

 BOSS_JOB_LIST
^^^^^^^^^^^^^^

* BOSS_JOB_LIST()
* construct()
* populateContent()
* setState(item, isActive)
* setupJob(selected)
* parseForGamerName(TF, str)

 BOSS_JOB_LIST_VIEW
^^^^^^^^^^^^^^^^^^^

* BOSS_JOB_LIST_VIEW()
* construct()
* populateContent()
* setupMessageBody()

 BREAKING_NEWS
^^^^^^^^^^^^^^

* BREAKING_NEWS()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SET_TEXT(titleT, subT)
* SET_SCROLL_TEXT(slot, id, str)
* DISPLAY_SCROLL_TEXT(slot, id, scrollSpeed)
* CLEAR_SCROLL_TEXT(slot)
* getTicker(slot)
* SHOW_STATIC(staticType)

 CALLSCREEN
^^^^^^^^^^^

* CALLSCREEN()
* construct()
* renderContainers()
* populateContent()
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* LOADCLIP(textureDict, targetMC)
* onLoadInit(target_mc)
* CLOSE_APP()
* parseForGamerName(TF, str)

 CAMERA_GALLERY
^^^^^^^^^^^^^^^

* CAMERA_GALLERY()
* INITIALISE(mc)
* getDisplayConfig()
* DISPLAY_VIEW(viewIndex)
* SHOW_PHOTO_FRAME(vis)
* SHOW_REMAINING_PHOTOS(vis)
* FLASH_PHOTO_FRAME()
* SET_REMAINING_PHOTOS(photosTaken, photosLeft)
* SET_FOCUS_LOCK(isVisible, str, iconVisible)
* OPEN_SHUTTER()
* CLOSE_SHUTTER()
* CLOSE_THEN_OPEN_SHUTTER()
* goTo(whichFrame)

 CAMERA_SHUTTER
^^^^^^^^^^^^^^^

* CAMERA_SHUTTER(mc)
* OPEN_SHUTTER()
* CLOSE_SHUTTER()
* CLOSE_THEN_OPEN_SHUTTER()
* goTo(whichFrame)

 CASINO_HEIST_BOARD_FINALE
^^^^^^^^^^^^^^^^^^^^^^^^^^

* CASINO_HEIST_BOARD_FINALE()
* initialise(mc)
* ADD_TODO_LIST_ITEM(itemText, isComplete)
* CLEAR_TODO_LIST()
* ADD_OPTIONAL_LIST_ITEM(itemText, isComplete)
* CLEAR_OPTIONAL_LIST()
* SET_PADLOCK(buttonID, isLocked)
* SET_TICK(buttonID, isTicked)
* SET_STAR(buttonID, isVisible)
* SET_BUTTON_VISIBLE(buttonID, isVisible)
* SET_BUTTON_ENABLED(buttonID, isEnabled)
* SET_BUTTON_IMAGE(buttonID, imageID)
* SET_BUTTON_GREYED_OUT(buttonID, isGreyedOut)
* SET_CREW_MEMBER(buttonID, name, image)
* SET_CREW_MEMBER_STATE(buttonID, isReady, headsetState)
* SET_CREW_CUT(buttonID, cut)
* SET_SELECTION_ARROWS_VISIBLE(buttonID, visibleState)
* SET_NOT_SELECTED_VISIBLE(buttonID, isVisible)
* SET_HEADINGS(approach, target, setupCost, potentialTake, supportCrewCut, entrance, exit, buyer, outfitIn, outfitOut)
* SET_CREW_PANEL_VISIBLE(isVisible)
* SET_LAUNCH_BUTTON_LABEL(label)
* SET_MAP_MARKERS(visibleGroup)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* SET_CURRENT_SELECTION(buttonID)
* GET_CURRENT_ROLLOVER()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* showScreen()
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)

 CASINO_HEIST_BOARD_PREP
^^^^^^^^^^^^^^^^^^^^^^^^

* CASINO_HEIST_BOARD_PREP()
* initialise(mc)
* ADD_TODO_LIST_ITEM(itemText, isComplete)
* CLEAR_TODO_LIST()
* ADD_OPTIONAL_LIST_ITEM(itemText, isComplete)
* CLEAR_OPTIONAL_LIST()
* SET_PADLOCK(buttonID, isLocked)
* SET_TICK(buttonID, isTicked)
* SET_BUTTON_VISIBLE(buttonID, isVisible)
* SET_BUTTON_ENABLED(buttonID, isEnabled)
* SET_BUTTON_IMAGE(buttonID, imageID)
* SET_BUTTON_GREYED_OUT(buttonID, isGreyedOut)
* SET_CREW_MEMBER(buttonID, name, skill, image, cut, weapon)
* SET_CREW_MEMBER_HIRED(buttonID, isHired)
* SET_MISSION(buttonID, image, title)
* SET_PURCHASED(buttonID, isPurchased)
* SET_STAR(buttonID, isVisible)
* SET_INSIDE_MAN(name, image)
* SET_SELECTION_ARROWS_VISIBLE(buttonID, visibleState)
* SET_HEADINGS(approach, target)
* ADD_APPROACH(buttonID, imageID, title, isComplete, isRequired, tapeLabel)
* REMOVE_APPROACH(buttonID)
* SET_SECURITY_PASS_VISIBLE(level)
* SET_POSTER_VISIBLE(buttonID, isVisible, numTicks, totalTickboxes)
* SET_MISSION_COMPLETION(buttonID, isVisible, numerator, denominator)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* SET_CURRENT_SELECTION(buttonID)
* GET_CURRENT_ROLLOVER()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* showScreen()
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)

 CASINO_HEIST_BOARD_SETUP
^^^^^^^^^^^^^^^^^^^^^^^^^

* CASINO_HEIST_BOARD_SETUP()
* initialise(mc)
* ADD_TODO_LIST_ITEM(itemText, isComplete)
* CLEAR_TODO_LIST()
* ADD_OPTIONAL_LIST_ITEM(itemText, isComplete)
* CLEAR_OPTIONAL_LIST()
* SET_POI_IMAGES()
* SET_PADLOCK(buttonID, isLocked)
* SET_EXTREME(buttonID, isExtreme)
* SET_STAR(buttonID, isVisible)
* SET_BUTTON_VISIBLE(buttonID, isVisible)
* SET_BUTTON_ENABLED(buttonID, isEnabled)
* SET_BUTTON_IMAGE(buttonID, imageID)
* SET_BUTTON_GREYED_OUT(buttonID, isGreyedOut)
* SET_TICK(buttonID, isTicked)
* SET_ACCESS_POINT_COMPLETION(buttonID, numAvailable, numComplete, isOptional)
* SET_SELECTION_ARROWS_VISIBLE(buttonID, visibleState)
* SET_BLUEPRINT_VISIBLE(isVisible)
* SET_TARGET_TYPE(targetType)
* SET_GRAPHICS_VISIBLE(isVisible)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* SET_CURRENT_SELECTION(buttonID)
* GET_CURRENT_ROLLOVER()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* showScreen()
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)

 CELLPHONE_ALERT_POPUP
^^^^^^^^^^^^^^^^^^^^^^

* CELLPHONE_ALERT_POPUP()
* INITIALISE(mc)
* CREATE_ALERT(iconID, newX, newY, titleString)
* CLEAR_ALL()

 CELLPHONE_BADGER
^^^^^^^^^^^^^^^^^

* CELLPHONE_BADGER()
* INITIALISE(mc)
* GET_CURRENT_SELECTION()
* SET_TITLEBAR_TIME(newHour, newMinute, newDay)
* SET_SLEEP_MODE(isSleepModeActive)
* SET_HEADER(newHeader)
* SET_SOFT_KEYS_COLOUR(buttonID, red, green, blue)
* SET_SOFT_KEYS(buttonID, isVisible, iconEnum, textLabel)
* toggleCellphoneButtonsVisible(isVisible)
* updateSoftKeys(currentClip)
* updateInfoBar(currentClip)
* COLOUR_BACKGROUND()
* REPLACE_BACKGROUND_IMAGE(image_enum, image_string)
* SET_BACKGROUND_IMAGE(image_enum, removeOnly)
* LOAD_BACKGROUND(txdString)
* SET_PROVIDER_ICON(icon_enum, signal_strength)
* SET_SIGNAL_STRENGTH(signal_strength)
* SET_THEME(themeID)
* SET_DATA_SLOT_EMPTY(viewID)
* SET_DATA_SLOT(viewID, slotID)
* DISPLAY_VIEW(_viewID, _currentID)
* CELLPHONE_APP(_currentID, _appString, isSameView)
* SHUTDOWN_MOVIE()
* LOAD_APP(fileToLoad)
* STREAM_RESPONSE(uid, fileToLoad)
* STREAM_RESPONSE_FAILED(uid)
* onLoadInit(target_mc)
* onLoadError(targetMC)
* REQUEST_REMOVE_APP(whichMC)
* REMOVE_CHILD_MOVIE(whichMC)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* SET_INPUT_EVENT(direction)
* createTransition(previousClip, currentClip)
* parseForGamerName(TF, str)

 CELLPHONE_CUTSCENE
^^^^^^^^^^^^^^^^^^^

* CELLPHONE_CUTSCENE()
* INITIALISE(mc)
* DISPLAY_VIEW(viewID)

 CELLPHONE_FACADE
^^^^^^^^^^^^^^^^^

* CELLPHONE_FACADE()
* INITIALISE(mc)
* GET_CURRENT_SELECTION()
* SET_TITLEBAR_TIME(newHour, newMinute, newDay)
* SET_SLEEP_MODE(isSleepModeActive)
* SET_HEADER(newHeader)
* COLOUR_HEADERBAR()
* SET_SOFT_KEYS_COLOUR(buttonID, red, green, blue)
* SET_SOFT_KEYS(buttonID, isVisible, iconEnum, textLabel)
* toggleCellphoneButtonsVisible(isVisible)
* updateSoftKeys(currentClip)
* updateInfoBar(currentClip)
* SET_BACKGROUND_IMAGE(image_enum)
* SET_PROVIDER_ICON(icon_enum, signal_strength)
* SET_SIGNAL_STRENGTH(signal_strength)
* SET_THEME(themeID)
* SET_DATA_SLOT_EMPTY(viewID)
* SET_DATA_SLOT(viewID, slotID)
* DISPLAY_VIEW(_viewID, _currentID)
* CELLPHONE_APP(_currentID, _appString, isSameView)
* SHUTDOWN_MOVIE()
* LOAD_APP(fileToLoad)
* STREAM_RESPONSE(uid, fileToLoad)
* STREAM_RESPONSE_FAILED(uid)
* onLoadInit(target_mc)
* onLoadError(target_mc)
* REQUEST_REMOVE_APP(whichMC)
* REMOVE_CHILD_MOVIE(whichMC)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* SET_INPUT_EVENT(direction)
* createTransition(previousClip, currentClip)
* parseForGamerName(TF, str)

 CELLPHONE_IFRUIT
^^^^^^^^^^^^^^^^^

* CELLPHONE_IFRUIT()
* INITIALISE(mc)
* GET_CURRENT_SELECTION()
* SET_TITLEBAR_TIME(newHour, newMinute, newDay)
* SET_SLEEP_MODE(isSleepModeActive)
* SET_HEADER(newHeader)
* SET_SOFT_KEYS_COLOUR(buttonID, red, green, blue)
* SET_SOFT_KEYS(buttonID, isVisible, iconEnum)
* toggleCellphoneButtonsVisible(isVisible)
* updateSoftKeys(currentClip)
* updateInfoBar(currentClip)
* REPLACE_BACKGROUND_IMAGE(image_enum, image_string)
* SET_BACKGROUND_IMAGE(image_enum, removeOnly)
* SET_BACKGROUND_CREW_IMAGE(_texture)
* LOAD_BACKGROUND(txdString)
* SET_PROVIDER_ICON(icon_enum, signal_strength)
* SET_SIGNAL_STRENGTH(signal_strength)
* SET_THEME(themeID)
* SET_DATA_SLOT_EMPTY(viewID)
* SET_DATA_SLOT(viewID, slotID)
* DISPLAY_VIEW(_viewID, _currentID)
* CELLPHONE_APP(_currentID, _appString, isSameView)
* SHUTDOWN_MOVIE()
* LOAD_APP(fileToLoad)
* STREAM_RESPONSE(uid, fileToLoad)
* STREAM_RESPONSE_FAILED(uid)
* onLoadInit(target_mc)
* onLoadError(targetMC)
* REQUEST_REMOVE_APP(whichMC)
* REMOVE_CHILD_MOVIE(whichMC)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* SET_INPUT_EVENT(direction)
* createIfruitTransition(previousClip, currentClip)
* IFRUIT_TRANSITION_IN(currentClip)
* parseForGamerName(TF, str)

 CELLPHONE_PROLOGUE
^^^^^^^^^^^^^^^^^^^

* CELLPHONE_PROLOGUE()
* INITIALISE(mc)
* GET_CURRENT_SELECTION()
* SET_TITLEBAR_TIME(newHour, newMinute, newDay)
* SET_SLEEP_MODE(isSleepModeActive)
* SET_HEADER(newHeader)
* SET_SOFT_KEYS_COLOUR(buttonID, ired, igreen, iblue, ialpha)
* SET_SOFT_KEYS(buttonID, isVisible, iconEnum, textLabel)
* updateSoftKeys(currentClip)
* updateInfoBar(currentClip)
* SET_UI_COLOUR(id, r, g, b)
* COLOUR_INFOBAR()
* SET_BACKGROUND_IMAGE(image_enum)
* SET_PROVIDER_ICON(icon_enum)
* SET_THEME(themeID)
* checkClassExists(viewID)
* SET_DATA_SLOT_EMPTY(viewID)
* SET_DATA_SLOT(viewID, slotID)
* GET_DATA(viewID)
* DISPLAY_VIEW(viewID, currentID)
* HOME_MENU(_currentID)
* CONTACT_LIST(_currentID)
* CALL_SCREEN(state)
* SHUTDOWN_MOVIE()
* SET_INPUT_EVENT(direction)
* createPrologueTransition(previousClip, currentClip)
* toggleCellphoneButtonsVisible(isVisible)

 CLIP_EDIT_TIMELINE
^^^^^^^^^^^^^^^^^^^

* CLIP_EDIT_TIMELINE()
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 CLIP_EDIT_TIMELINE_CLICK_REGION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


 CLUBHOUSE_NAME
^^^^^^^^^^^^^^^

* CLUBHOUSE_NAME()
* INITIALISE(mc)
* SET_CLUBHOUSE_NAME(str, colourIndex, fontIndex)

 COL_TYPE_BASIC_PAGE
^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_BASIC_PAGE()
* clearBlipLayer()

 COL_TYPE_IMG_PROJ_INFO
^^^^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_IMG_PROJ_INFO()

 COL_TYPE_IMG_TWELVE
^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_IMG_TWELVE()
* loadCompleted()

 COL_TYPE_LIST
^^^^^^^^^^^^^^

* COL_TYPE_LIST()
* initColours(receivedColours)
* SetAsSelected(isSelected, onlyOneOption)
* SetColourState(stateId)
* setGreyedOut()
* removeGreyOut()
* HideBackground()
* setIconVisible(value)
* switchColour()
* shortenAndSetStr(str, tf, maxChars, isItemTitle)
* colourThisToBlack()
* colourThisToBlue()
* colourThisToRed()
* updateColours()
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 COL_TYPE_LIST_HELP
^^^^^^^^^^^^^^^^^^^

* COL_TYPE_LIST_HELP()
* initColours(receivedColours)
* clearBlipLayer()

 COL_TYPE_LIST_LONG_AUDIO
^^^^^^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_LIST_LONG_AUDIO()
* SetAnimatedAudioVisibility(isVisible)
* SetAnimatedAudioPlaying(isPlaying)
* SetAsSelected(isSelected)

 COL_TYPE_LIST_PROJECT_SIZE
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_LIST_PROJECT_SIZE()
* initColors(receivedColours)
* setBar(value)
* setHelpTopVisibility(isVisible)
* clearBlipLayer()

 COL_TYPE_LIST_SCROLL
^^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_LIST_SCROLL()
* INIT_LIST_SCROLL_BUTTONS()
* dispose()
* initColors(receivedColours)
* onMouseRelease(dir)
* sendMouseEvent(evt, dir)

 COL_TYPE_LIST_SCROLL_AUDIO
^^^^^^^^^^^^^^^^^^^^^^^^^^^


 COL_TYPE_LOAD_PROJ_INFO
^^^^^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_LOAD_PROJ_INFO()
* updateUploadProgress(label)
* setUploadStatusState(stateId)
* initColors(receivedColours)
* showUploadProgress(isVisible)
* shortenAndSetStr(str, tf, maxChars)

 COL_TYPE_TEXT_PLACEMENT
^^^^^^^^^^^^^^^^^^^^^^^^

* COL_TYPE_TEXT_PLACEMENT()

 COLOUR_SWITCHER
^^^^^^^^^^^^^^^^

* COLOUR_SWITCHER()
* INITIALISE(mc)
* debug()
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_IS_PC(_pcActiveOn)
* SET_TITLE(str)
* itemSetData(i, cMC, cData)

 CONTACTLIST
^^^^^^^^^^^^

* CONTACTLIST()
* construct()
* renderContainers()
* populateContent()
* createContact(index)
* removeAllContacts()
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* setState(item, isActive)
* navigate(direction)
* getRowAsPercentage(rowNumber)
* setScrollBarVisibility(isVisible)
* GET_CURRENT_SELECTION()
* SHOW()
* HIDE()
* REMOVE()
* CLOSE_APP()

 CONTROLLER_TEST
^^^^^^^^^^^^^^^^

* CONTROLLER_TEST()
* INITIALISE(mc)
* resetIcon(mc)
* growIcon(mc)
* resetDpad(mc)
* playDpad(mc)
* SET_INPUT_EVENT(direction)
* SET_ANALOG_STICK_INPUT(isLeftStick, mouseX, mouseY)
* SET_MOUSE_INPUT(mouseX, mouseY)
* SET_RELATIVE_INPUT(scaledRelMouseX, scaledRelMouseY)
* SET_MOUSE_BUTTON_STATES(pressedButtons)
* SET_MOUSE_WHEEL(mouseWheel)
* SET_MOUSEBOX_VISIBLE(value)
* SET_ANALOG_TRIGGER_INPUT_VISIBLE(value)
* SET_ANALOG_TRIGGER_INPUT(isLeftTrigger, normalizedInputValue)
* drawMouseWheel()
* clamp(value, min, max)

 COUNTDOWN
^^^^^^^^^^

* COUNTDOWN()
* INITIALISE(mc)
* SET_MESSAGE(newString, r, g, b, isMP)
* FADE_SP(newString, r, g, b)
* FADE_MP(newString, r, g, b)
* OVERRIDE_FADE_DURATION(newFadeDuration)
* IS_COUNTDOWN_VISIBLE()
* SET_DIRECTION(direction, r, g, b)
* SET_COUNTDOWN_LIGHTS(value)
* initCountdown()
* setCountdownLights(value)

 COVERT_OPS
^^^^^^^^^^^

* COVERT_OPS()
* initialise(mc)
* ACTIVATE()
* DEACTIVATE()
* SET_PLAYER_DATA(gamerTag)
* ADD_MISSION(id, name, description, txd, lockNum, enabled, cashBonus, rpBonus)
* UPDATE_COOLDOWN(remainingSeconds)
* SHOW_OVERLAY(titleLabel, messageLabel, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_SCREEN_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* TXD_HAS_LOADED(txd, success, id)

 CUSTOM_WARNING_SCREEN
^^^^^^^^^^^^^^^^^^^^^^

* CUSTOM_WARNING_SCREEN()
* INITIALISE(mc)
* SHOW_CUSTOM_WARNING_SCREEN()
* HIDE_CUSTOM_WARNING_SCREEN(msecs)
* SET_SELECTED_INDEX()
* debug()

 DASHBOARD
^^^^^^^^^^

* DASHBOARD()
* INITIALISE(mc)
* getDialAngle(minRot, maxRot, scale, isClockwise)
* SET_DASHBOARD_LIGHTS(indicator_left, indicator_right, handbrakeLight, engineLight, ABSLight, petrolLight, oilLight, headlights, fullBeam, batteryLight, shiftLight1, shiftLight2, shiftLight3, shiftLight4, shiftLight5)
* SET_DASHBOARD_DIALS(RPM, speed, fuel, temp, vacuum, boost, oilTemperature, oilPressure, waterTemp, curGear)
* TOGGLE_BACKGROUND_VISIBILITY(isVisible)
* SET_VEHICLE_TYPE(eType)
* SET_RADIO(tuning, station, artist, song)
* initStationText(tf, text)
* initScrollingTextfield(tf, text)
* debug()

 DESKTOP_PC
^^^^^^^^^^^

* DESKTOP_PC()
* INITIALISE(mc)
* debug()
* getKeys()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef)
* initScreenLayout()
* ADD_PROGRAM(i, enum, lbl)
* RUN_PROGRAM(id)
* SET_DATA_SLOT(i, id, x, y, t)
* OPEN_POPUP(i)
* CLOSE_POPUP(i)
* OPEN_ANTIVIRUS(i, promptText)
* SET_INPUT_EVENT(direction)
* IS_PC_NEEDED()
* SET_SCAN_BAR(percent)
* PLAY_SCAN_ANIM(bool)
* addButtons(m, addOnce)
* activateButtons(m, b)
* removeButtons(m)
* SET_SNAP_SPEED(s)
* SET_CURSOR(vx, vy)
* MOVE_CURSOR(vx, vy)
* checkUnderCursor()
* snapToButton()
* snapToButtonComplete()
* testList(list)
* resetUnderCursor()
* cursorClick()
* LAST_POPUP_CLOSED()
* openApp(i)
* closeApp(id)
* RESTART_MOVIE()

 DIAL_BANSHEE
^^^^^^^^^^^^^

* DIAL_BANSHEE(mc)

 DIAL_BOBCAT
^^^^^^^^^^^^

* DIAL_BOBCAT(mc)

 DIAL_CAVALCADE
^^^^^^^^^^^^^^^

* DIAL_CAVALCADE(mc)

 DIAL_COMET
^^^^^^^^^^^

* DIAL_COMET(mc)

 DIAL_DUKES
^^^^^^^^^^^

* DIAL_DUKES(mc)

 DIAL_FACTION
^^^^^^^^^^^^^

* DIAL_FACTION(mc)

 DIAL_FELTZER
^^^^^^^^^^^^^

* DIAL_FELTZER(mc)

 DIAL_FEROCI
^^^^^^^^^^^^

* DIAL_FEROCI(mc)

 DIAL_FUTO
^^^^^^^^^^

* DIAL_FUTO(mc)

 DIAL_GENTAXI
^^^^^^^^^^^^^

* DIAL_GENTAXI(mc)

 DIAL_INFERNUS
^^^^^^^^^^^^^^

* DIAL_INFERNUS(mc)

 DIAL_MAVERICK
^^^^^^^^^^^^^^

* DIAL_MAVERICK(mc)

 DIAL_MOTORBIKE
^^^^^^^^^^^^^^^

* DIAL_MOTORBIKE(mc)

 DIAL_PEYOTE
^^^^^^^^^^^^

* DIAL_PEYOTE(mc)

 DIAL_RACE
^^^^^^^^^^

* DIAL_RACE(mc)

 DIAL_RUINER
^^^^^^^^^^^^

* DIAL_RUINER(mc)

 DIAL_SPEEDO
^^^^^^^^^^^^

* DIAL_SPEEDO(mc)

 DIAL_SULTAN
^^^^^^^^^^^^

* DIAL_SULTAN(mc)

 DIAL_SUPERGT
^^^^^^^^^^^^^

* DIAL_SUPERGT(mc)

 DIAL_TAILGATER
^^^^^^^^^^^^^^^

* DIAL_TAILGATER(mc)

 DIAL_TRUCK
^^^^^^^^^^^

* DIAL_TRUCK(mc)

 DIAL_TRUCKDIGI
^^^^^^^^^^^^^^^

* DIAL_TRUCKDIGI(mc)

 DIAL_ZTYPE
^^^^^^^^^^^

* DIAL_ZTYPE(mc)

 DIGISCANNER
^^^^^^^^^^^^

* DIGISCANNER()
* INITIALISE(mc)
* SET_DISTANCE(distance)
* SET_COLOUR()
* lightsManager()
* flashOn()
* flashOff(mc)
* stopFlash()

 DIGITAL_CAMERA
^^^^^^^^^^^^^^^

* DIGITAL_CAMERA()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SHOW_REMAINING_PHOTOS(vis)
* SET_REMAINING_PHOTOS(photosTaken, photosLeft)
* SHOW_PHOTO_BORDER(vis, rotation, xpos, ypos, xscale, yscale)
* SHOW_PHOTO_FRAME(vis)
* SHOW_FOCUS_LOCK(isVisible, str)
* OPEN_SHUTTER(_shutterSpeed)
* CLOSE_SHUTTER(_shutterSpeed)
* CLOSE_THEN_OPEN_SHUTTER()
* goTo(whichFrame)

 DISRUPTION_LOGISTICS
^^^^^^^^^^^^^^^^^^^^^

* DISRUPTION_LOGISTICS()
* initialise(mc)
* ACTIVATE()
* DEACTIVATE()
* APP_IS_DEACTIVATED()
* SET_STATS(userName, orgName, txd, bunkerName, bunkerLocation, status, stockLevel, researchProgress, suppliesLevel, totalEarnings, totalSales, resupplySuccessRate, sellSuccessRateBC, sellSuccessRateLS, numUnitsManufactured, numResearchUnlocked, numResearchTotal, staffDistribution)
* SET_RESUPPLIES(resupplyCost, resupplyButtonState, stealButtonState, resupplySaleCost)
* SET_UPGRADES(upgrade1Cost, upgrade1ButtonState, upgrade2Cost, upgrade2ButtonState, upgrade3Cost, upgrade3ButtonState, upgrade1SaleCost, upgrade2SaleCost, upgrade3SaleCost)
* SET_RESEARCH(fastTrackCost, researchProgress, texture, state, description, heading, fastTrackSaleCost)
* ADD_RESEARCH_UNLOCKABLE(state, texture, title, description, index)
* ACTIVATE_FAST_TRACK()
* SET_SELL_PRICES(sellLSValue, sellBCValue)
* SET_BUTTON_STATES(setup, resupply, research, staff, upgrades, shutDown, restart, sell, fastTrack, purchaseSupplies)
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(message, accept, cancel, image, title)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* updateButtons()
* disableAllButtons()
* enableAllButtons()
* TXD_HAS_LOADED(txd, success, id)

 DJ
^^^

* DJ()

 DRILLING
^^^^^^^^^

* DRILLING()
* INITIALISE(mc)
* SET_SPEED(speed)
* SET_DEPTH(depth)
* SET_TEMPERATURE(temperature)

 DRONE_CAM
^^^^^^^^^^

* DRONE_CAM()
* INITIALISE(mc)
* initLayout()
* SET_RETICLE_IS_VISIBLE(isVisible)
* SET_ZOOM_METER_IS_VISIBLE(isVisible)
* SET_HEADING_METER_IS_VISIBLE(isVisible)
* SET_SHOCK_METER_IS_VISIBLE(isVisible)
* SET_DETONATE_METER_IS_VISIBLE(isVisible)
* SET_TRANQUILIZE_METER_IS_VISIBLE(isVisible)
* SET_BOOST_METER_IS_VISIBLE(isVisible)
* SET_MISSILE_METER_IS_VISIBLE(isVisible)
* SET_EMP_METER_IS_VISIBLE(isVisible)
* SET_INFO_LIST_IS_VISIBLE(isVisible)
* SET_SOUND_WAVE_IS_VISIBLE(isVisible)
* SET_BOTTOM_LEFT_CORNER_IS_VISIBLE(isVisible)
* SET_WARNING_IS_VISIBLE(isVisible)
* SET_ZOOM_LABEL(index, label)
* SET_ZOOM(level)
* SET_HEADING(angle)
* SET_SHOCK_PERCENTAGE(percent)
* SET_DETONATE_PERCENTAGE(percent)
* SET_TRANQUILIZE_PERCENTAGE(percent)
* SET_BOOST_PERCENTAGE(percent)
* SET_MISSILE_PERCENTAGE(percent)
* SET_EMP_PERCENTAGE(percent)
* SET_INFO_LIST_DATA(rank, earnings, kills, deaths, vehicle, accuracy, radioStation, weapon, privateDances, numHoes, gamertag)
* ATTENUATE_SOUND_WAVE(scalar)
* SET_RETICLE_PERCENTAGE(percent)
* SET_RETICLE_ON_TARGET(isOnTarget)
* SET_RETICLE_STATE(state)
* SET_WARNING_FLASH_RATE(normRate)

 ECG_MONITOR
^^^^^^^^^^^^

* ECG_MONITOR()
* INITIALISE(mc)
* removeBeat(args)
* SET_HEART_RATE(rate)
* SET_HEART_BEAT(speed)
* SET_HEALTH(amount)
* SET_ECG_HEALTH(amount)
* SET_COLOUR(r, g, b)

 ECOMMERCE_STORE
^^^^^^^^^^^^^^^^

* ECOMMERCE_STORE()
* INITIALISE(mc)
* getHudColours()
* BUILD_MENU(menuIndex)
* MENU_STATE(menuIndex)
* REMOVE_COLUMN(_column)
* SET_DATA_SLOT_EMPTY(_column, _slot)
* SET_DATA_SLOT()
* DISPLAY_DATA_SLOT(_column)
* UPDATE_DATA_SLOT(_column, _slotIndex)
* HIDE_COLUMN2(vis)
* SET_HEADER_COLOUR()
* SET_STATUS_COLOURS()
* SET_CONTENTIMAGE_SIZE(_visItems)
* SET_HEADER_TITLE(str)
* SET_COLUMN_TITLE(columnIndex, str)
* SET_MENU_HEADER_TEXT(columnIndex, str)
* SET_HEADING_DETAILS(str1, str2, str3, isSingleplayer, crewname)
* SET_CREW_IMG(txd, crewTexturePath, show)
* loadedCrewImg()
* SET_CHAR_IMG(txd, charTexturePath, show)
* loadedCharImg()
* adjustHeaderPositions()
* SHOW_PLAYSTATION_LOGO(vis)
* SET_SHOP_LOGO(_logo)
* SHOW_SHOP_LOGO(vis)
* SET_DESCRIPTION(column, priceTitle, itemPrice, numPlayers, statusText, statusColour, priceVis, playersVis, statusVis)
* HIGHLIGHT_ITEM(_column, _itemIndex)
* HIGHLIGHT_COLUMN(_column)
* GET_CURRENT_SELECTION(_column)
* GET_CURRENT_START_INDEX(_column)
* GET_CURRENT_END_INDEX(_column)
* GET_CURRENT_COLUMN()
* DISPLAY_ERROR_MESSAGE(titleStr, msgStr)
* colouriseHeader()
* SHUTDOWN_MOVIE()
* SET_INPUT_EVENT(direction)
* SET_INPUT_EVENT_CIRCLE()
* SET_INPUT_EVENT_CROSS()
* SET_ANALOG_STICK_INPUT(isLeftStick, inputX, inputY)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* traceOut(str)

 EDITOR_SHUTTER
^^^^^^^^^^^^^^^

* EDITOR_SHUTTER()
* OPEN_SHUTTER()
* CLOSE_SHUTTER()
* CLOSE_THEN_OPEN_SHUTTER()
* goTo(whichFrame)

 EMAIL_LIST
^^^^^^^^^^^

* EMAIL_LIST()
* construct()
* populateContent()
* setState(item, isActive)

 EMAIL_RESPONSE
^^^^^^^^^^^^^^^

* EMAIL_RESPONSE()
* construct()
* populateContent()
* setState(item, isActive)

 EMAIL_VIEW
^^^^^^^^^^^

* EMAIL_VIEW()
* construct()
* populateContent()
* setupMessageBody()
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* LOADCLIP(textureDict, targetMC)
* onLoadInit(target_mc)
* CLEAN_UP_DATA()

 GRID_LAYOUT
^^^^^^^^^^^^

* GRID_LAYOUT(mc)
* INITIALISE(mc)
* SET_INFO(b)
* SET_SAFE(i)
* SET_SCALE(i)

 HACKER_TRUCK_DESKTOP
^^^^^^^^^^^^^^^^^^^^^

* HACKER_TRUCK_DESKTOP()
* initialise(mc)
* UPDATE_MISSION(index, isAvailable, cooldown)
* CLEAR_JOBS()
* ADD_JOB(index, title, value, valueType, tooltip, isAvailable, salePrice)
* SHOW_JOB_OVERLAY(missionIndex, title)
* HIDE_JOB_OVERLAY()
* UPDATE_COOLDOWN(index, value)
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)

 HACKING_PC
^^^^^^^^^^^

* HACKING_PC()
* INITIALISE(mc)
* SET_LABELS()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* initScreenLayout()
* SET_BACKGROUND(bgEnum)
* SET_INPUT_EVENT(direction)
* SET_INPUT_EVENT_SELECT()
* SET_INPUT_EVENT_BACK()
* ADD_PROGRAM(i, enum, lbl)
* RUN_PROGRAM(id)
* ADD_BUTTONS(m)
* ACTIVATE_BUTTONS(m, b)
* REMOVE_BUTTONS(m)
* SET_SNAP_SPEED(s)
* SET_CURSOR(vx, vy)
* MOVE_CURSOR(vx, vy)
* SET_CURSOR_VISIBILITY(isVisible)
* checkUnderCursor()
* snapToButton()
* snapToButtonComplete()
* testList(list)
* RESET_UNDER_CURSOR()
* CURSOR_CLICK(direction)
* openApp(i)
* closeApp(id)
* setDesktopIconsActive(a)
* OPEN_APP(id)
* CLOSE_APP()
* OPEN_LOADING_PROGRESS(bool)
* SET_LOADING_PROGRESS(percent, showPercent)
* SET_LOADING_TIME(secs, label)
* SET_LOADING_MESSAGE(msg, size)
* OPEN_DOWNLOAD(bool)
* OPEN_ERROR_POPUP(bool, msg)
* SET_IP_OUTCOME(success, winStr)
* SET_ROULETTE_OUTCOME(success, outcomeStr)
* SET_ROULETTE_WORD(wordStr)
* STOP_ROULETTE()
* RESET_ROULETTE()
* SET_COUNTDOWN(m, s, ms)
* SET_SPEED(speed)
* SET_KEY_REPEAT_DELAY(kDelay)
* SET_COLUMN_SPEED(columnIndex, speed)
* SET_LIVES(lives, total)
* SHOW_LIVES(vis)
* RESTART_MOVIE()
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* removeBackground()
* loadBackground(textureDict)
* onLoadInit(target_mc)
* SHUTDOWN_MOVIE()

 HANGAR_CARGO
^^^^^^^^^^^^^

* HANGAR_CARGO()
* initialise(mc)
* SET_STATS(organisationName, location, stealsCompleted, stealSuccessRate, salesCompleted, salesSuccessRate, rivalCratesStolen, saleEarnings, bonusEarnings, filledSpace, totalSpace, sellAllPrice)
* ADD_CARGO(type, currentStockLevel, totalStockLevel, bonusPercent, sellPrice)
* ADD_ACTIVE_ORGANISATION(name)
* REMOVE_ACTIVE_ORGANISATION(name)
* UPDATE_STEAL_COOLDOWN(cargo1RemainingSeconds, cargo2RemainingSeconds, cargo3RemainingSeconds, cargo4RemainingSeconds, cargo5RemainingSeconds, cargo6RemainingSeconds, cargo7RemainingSeconds, cargo8RemainingSeconds)
* UPDATE_SELL_COOLDOWN(remainingSeconds, totalSeconds)
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* updateButtons()

 HEIST_AGENCY
^^^^^^^^^^^^^

* HEIST_AGENCY()
* INITIALISE(mc)
* debug()
* getKeys()
* CREATE_VIEW(viewIndex, viewType, xp, yp)
* REPOSITION_VIEW(viewIndex, xp, yp)
* SET_LABELS(_weaponname, _jobcut, _accuracy)
* setText(tf, str)
* SHOW_VIEW(_viewIndex, _show)
* SET_TODO(_viewIndex, _itemIndex, _checked)
* RegisterHeistAsset(enum, mc)
* SHOW_HEIST_ASSET(enum, visible, frame, x, y)

 HEIST_DOCKS
^^^^^^^^^^^^

* HEIST_DOCKS()
* INITIALISE(mc)
* debug()
* getKeys()
* CREATE_VIEW(viewIndex, viewType, xp, yp)
* REPOSITION_VIEW(viewIndex, xp, yp)
* SET_LABELS(_weaponname, _jobcut, _accuracy)
* SHOW_VIEW(_viewIndex, _show)
* SET_TODO(_viewIndex, _itemIndex, _checked)
* RegisterHeistAsset(enum, mc)
* SHOW_HEIST_ASSET(enum, visible, frame, x, y)

 HEIST_ENDSCREEN
^^^^^^^^^^^^^^^^

* HEIST_ENDSCREEN()
* INITIALISE(mc)
* SHOW_PIECHART_NUMBERS(vis)
* SET_PIECHART_COLOURS(playerNum, R1, G1, B1)
* SET_PIE_CHART()
* drawArc(pieMC, rotation, percent, pieNumber, _r, _g, _b)

 HEIST_FINALE
^^^^^^^^^^^^^

* HEIST_FINALE()
* INITIALISE(mc)
* debug()
* getKeys()
* CREATE_VIEW(viewIndex, viewType, xp, yp)
* REPOSITION_VIEW(viewIndex, xp, yp)
* SET_LABELS(_weaponname, _jobcut, _accuracy)
* SHOW_VIEW(_viewIndex, _show)
* SET_TODO(_viewIndex, _itemIndex, _checked)
* RegisterHeistAsset(enum, mc)
* SHOW_HEIST_ASSET(enum, visible, frame, x, y)

 HEIST_JEWELLERY
^^^^^^^^^^^^^^^^

* HEIST_JEWELLERY()
* INITIALISE(mc)
* debug()
* getKeys()
* CREATE_VIEW(viewIndex, viewType, xp, yp)
* REPOSITION_VIEW(viewIndex, xp, yp)
* SET_LABELS(_weaponname, _jobcut, _accuracy)
* SHOW_VIEW(_viewIndex, _show)
* SET_TODO(_viewIndex, _itemIndex, _checked)
* RegisterHeistAsset(enum, mc)
* SHOW_HEIST_ASSET(enum, visible, frame, x, y)

 HEIST_PALETO
^^^^^^^^^^^^^

* HEIST_PALETO()
* INITIALISE(mc)
* debug()
* getKeys()
* CREATE_VIEW(viewIndex, viewType, xp, yp)
* REPOSITION_VIEW(viewIndex, xp, yp)
* SET_LABELS(_weaponname, _jobcut, _accuracy)
* SHOW_VIEW(_viewIndex, _show)
* SET_TODO(_viewIndex, _itemIndex, _checked)
* RegisterHeistAsset(enum, mc)
* SHOW_HEIST_ASSET(enum, visible, frame, x, y)

 HEIST2_CELEBRATION
^^^^^^^^^^^^^^^^^^^

* HEIST2_CELEBRATION()
* INITIALISE(mc, type)
* registerSyncedMovie(id, sequenceTypeBit)
* syncPointClear(id)
* PAUSE()
* SET_PAUSE_DURATION()
* CREATE_STAT_WALL(id, bgColourId, sfxId)
* ADD_BACKGROUND_TO_WALL(id, alpha, sideTextureId)
* ADD_MISSION_RESULT_TO_WALL(id, missionTextLabel, passFailTextLabel, messageLabel, isMessageRawText, isPassFailRawText, isMissionTextRawText)
* ADD_COMPLETE_MESSAGE_TO_WALL(id, missionTextLabel, completeTextLabel, messageLabel, isMessageRawText, isCompleteRawText, isMissionTextRawText)
* CREATE_STAT_TABLE(id, stepId)
* ADD_STAT_TO_TABLE(id, stepId, name, value, isNameRawText, isValueRawText, isTotalRow, isStatValueTime, colourId)
* ADD_STAT_TABLE_TO_WALL(id, stepId)
* SHOW_STAT_WALL(id)
* CREATE_INCREMENTAL_CASH_ANIMATION(id, stepId)
* ADD_INCREMENTAL_CASH_WON_STEP(id, stepId, startDollars, finishDollars, topText, bottomText, rightHandStat, rightHandIcon, soundType)
* ADD_INCREMENTAL_CASH_ANIMATION_TO_WALL(id, stepId)
* ADD_JOB_POINTS_TO_WALL(id, points, xAlign)
* ADD_REP_POINTS_AND_RANK_BAR_TO_WALL(id, repPointsGained, startRepPoints, minRepPointsForRank, maxRepPointsForRank, currentRank, nextRank, rank1Txt, rank2Txt)
* PAUSE_BEFORE_PREVIOUS_LAYOUT()
* ADD_CASH_DEDUCTION(id, title, description, value)
* ADD_CASH_WON_TO_WALL(id, statLabel, finalValue, startValue, xAlign, isRawText)
* ADD_CASH_TO_WALL(id, value, xAlign)
* CLEANUP(id)
* createSequence(bgColour, sfxId, id)
* getLocalisedText(label)
* getColourFromId(id)

 HELI_CAM
^^^^^^^^^

* HELI_CAM()
* INITIALISE(mc)
* initScreenLayout()
* SET_COMPASS_POINT_POS(mc, a, index)
* SET_CAM_HEADING(a)
* SET_CAM_FOV(a)
* SET_CAM_ALT(a)
* SET_ALT_FOV_HEADING(a, f, h)
* SET_CAM_LOGO(value)
* SET_AUDIO_STATES(smallLine, mediumLine, largeLine)

 HELP_TEXT
^^^^^^^^^^

* HELP_TEXT()

 HELPTEXT
^^^^^^^^^


 HOMEMENU
^^^^^^^^^


 HOMEMENU_BADGER
^^^^^^^^^^^^^^^^

* HOMEMENU_BADGER()
* construct()
* populateContent()
* navigate(direction)
* GET_CURRENT_SELECTION()
* setIcon(target, menuIconFrameEnum, iconAlpha)
* setState(item, isActive)

 HOMEMENU_FACADE
^^^^^^^^^^^^^^^^

* HOMEMENU_FACADE()
* construct()
* populateContent()
* navigate(direction)
* GET_CURRENT_SELECTION()
* setIcon(target, menuIconFrameEnum, iconAlpha)
* setState(item, isActive)

 HOMEMENU_IFRUIT
^^^^^^^^^^^^^^^^

* HOMEMENU_IFRUIT()
* construct()
* populateContent()
* navigate(direction)
* GET_CURRENT_SELECTION()
* setIcon(target, menuIconFrameEnum, iconAlpha)
* setState(item, isActive)

 HUD_AREA_NAME
^^^^^^^^^^^^^^

* HUD_AREA_NAME()
* READY(id)
* SET_AREA_NAME(newName)
* FORCE_SHOW(_forceShow)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_AREA_VEHICLE_STREET_NAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* HUD_AREA_VEHICLE_STREET_NAME()
* INITIALISE(mc)
* READY(id)
* SET_AREA_NAME(params)
* SET_STREET_NAME(params)
* SET_VEHICLE_NAME(params)
* SET_NAME(params)
* FORCE_SHOW(_forceShow)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_CASH
^^^^^^^^^

* HUD_CASH()
* INITIALISE(mc)
* READY(id)
* SET_PLAYER_CASH(params)
* SET_PLAYER_CHIPS(params)
* SET_PLAYER_CASH_WITH_STRING(params)
* SET_PLAYER_MP_CASH(params)
* SET_PLAYER_MP_CASH_WITH_STRING(params)
* REMOVE_PLAYER_MP_CASH()
* SHOW(bSkipFade)
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()
* getTopCompOffset()
* getBottomCompOffset()
* SET_PLAYER_CASH_CHANGE(params)
* SET_MP_MESSAGE(params)

 HUD_CASH_CHANGE
^^^^^^^^^^^^^^^^

* HUD_CASH_CHANGE()
* INITIALISE(mc)
* READY(id)
* SET_PLAYER_CASH_CHANGE(params)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_CASH_CHANGED
^^^^^^^^^^^^^^^^^


 HUD_CHIPS
^^^^^^^^^^

* HUD_CHIPS()
* INITIALISE(mc)
* READY(id)
* SET_PLAYER_CASH(params)
* SET_PLAYER_CHIPS(params)
* SET_PLAYER_CASH_WITH_STRING(params)
* SET_PLAYER_MP_CASH(params)
* SET_PLAYER_MP_CASH_WITH_STRING(params)
* REMOVE_PLAYER_MP_CASH()
* SHOW(bSkipFade)
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()
* getTopCompOffset()
* getBottomCompOffset()
* SET_PLAYER_CASH_CHANGE(params)
* SET_PLAYER_CHIP_CHANGE(params)
* SET_MP_MESSAGE(params)

 HUD_CHIPS_CHANGED
^^^^^^^^^^^^^^^^^^


 HUD_COMPONENT
^^^^^^^^^^^^^^

* HUD_COMPONENT()
* INITIALISE(mc)
* READY(id)
* getTopCompOffset()
* getBottomCompOffset()
* SET_HUD(hud)
* destroy()

 HUD_DIRECTOR_MODE
^^^^^^^^^^^^^^^^^^

* HUD_DIRECTOR_MODE()
* INITIALISE(mc)
* READY(id)
* SET_DIRECTOR_MODE_TEXT(params)
* REMOVE_DIRECTOR_MODE_TEXT(params)
* SHOW()
* FORCE_FADE_OUT(params)
* HIDE()
* REMOVE()
* getBottomCompOffset()

 HUD_DISTRICT_NAME
^^^^^^^^^^^^^^^^^^

* HUD_DISTRICT_NAME()
* READY(id)
* SET_DISTRICT_NAME(newName)
* FORCE_SHOW(_forceShow)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_DRUGS_PURSE
^^^^^^^^^^^^^^^^

* HUD_DRUGS_PURSE()
* SET_DRUG_AMOUNT_AND_TYPE(params)
* REMOVE_DRUG_PURSE()

 HUD_FLOATING_HELP_TEXT
^^^^^^^^^^^^^^^^^^^^^^^

* HUD_FLOATING_HELP_TEXT()
* INITIALISE(mc)
* READY(id)
* clearBlipLayer()
* SET_HELP_TEXT_POSITION(params)
* SET_HELP_TEXT_OFFSCREEN(params)
* toggleOffScreen(isHelpTextVisible)
* SET_HELP_TEXT_STYLE(params)
* SET_HELP_TEXT(params)
* SET_HELP_TEXT_RAW(params)
* SET_BACKGROUND_SIZE()
* FADE_IN()
* STAY_ON_SCREEN()
* CLEAR_HELP_TEXT(params)
* CLEAR_HELP_TEXT_NOW(params)
* FADE_OUT()
* REMOVE()
* COORDS_TO_SCREEN(posX, posY)
* clamp(value, min, max)

 HUD_FLOATING_HELP_TEXT_1
^^^^^^^^^^^^^^^^^^^^^^^^^

* HUD_FLOATING_HELP_TEXT_1()
* INITIALISE(mc)

 HUD_FLOATING_HELP_TEXT_2
^^^^^^^^^^^^^^^^^^^^^^^^^

* HUD_FLOATING_HELP_TEXT_2()

 HUD_HELP_TEXT
^^^^^^^^^^^^^^

* HUD_HELP_TEXT()
* INITIALISE(mc)
* clearBlipLayer()
* READY(id)
* SET_HELP_TEXT(params)
* SET_HELP_TEXT_RAW(params)
* setHelpText(params, bSetWithIcons)
* calculateOnScreenDuration(str)
* SET_OVERRIDE_DURATION(params)
* toggleOffScreen(isHelpTextVisible)
* SET_HELP_TEXT_STYLE(params)
* SET_BACKGROUND_SIZE()
* FADE_IN()
* STAY_ON_SCREEN()
* CLEAR_HELP_TEXT(params)
* CLEAR_HELP_TEXT_NOW(params)
* REMOVE()
* UNLOAD_MOVIE()
* logHelpTextDisplayStatus(Name)

 HUD_HELP_TEXT_BIG
^^^^^^^^^^^^^^^^^^


 HUD_MISSION_PASSED_MESSAGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* HUD_MISSION_PASSED_MESSAGE()
* READY(id)
* SET_MISSION_PASSED_MESSAGE(params)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_MP_CASH
^^^^^^^^^^^^

* HUD_MP_CASH()
* INITIALISE(mc)
* READY(id)
* SET_PLAYER_MP_CASH(params)
* SHOW()
* STAY_ON_SCREEN()
* REMOVE_PLAYER_MP_CASH()
* HIDE()
* REMOVE()

 HUD_MP_INVENTORY
^^^^^^^^^^^^^^^^^

* HUD_MP_INVENTORY()
* INITIALISE(mc)
* SHOW_MP_INVENTORY_ITEM_WITH_TEXT(params)
* SHOW_MP_INVENTORY_ITEM(params)
* REMOVE_MP_INVENTORY_ITEM()

 HUD_MP_MESSAGE
^^^^^^^^^^^^^^^

* HUD_MP_MESSAGE()
* READY(id)
* SET_MP_MESSAGE(params)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_MULTIPLAYER_CHAT
^^^^^^^^^^^^^^^^^^^^^

* HUD_MULTIPLAYER_CHAT()
* INITIALISE(mc)
* READY(id)
* PAGE_UP()
* PAGE_DOWN()
* ADD_TEXT(text)
* SET_FOCUS(focus, TypeMode)
* SET_TYPING_DONE()
* SET_STREET_NAME(newName)
* FORCE_SHOW(_forceShow)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_PLAYER_SWITCH_ALERT
^^^^^^^^^^^^^^^^^^^^^^^^

* HUD_PLAYER_SWITCH_ALERT()
* INITIALISE(mc)
* CLEANUP_PLAYER_SWITCH_ALERT()
* ADD_PLAYER_TO_SWITCH(params)
* SET_PLAYER_SWITCH_WITH_HINT_AND_CHARACTER(params)
* START_PLAYER_SWITCH_LOOP()
* SET_PLAYER_SWITCH_VISIBLE_STATE(params)
* FLASH_ON()
* FLASH_OFF()
* BLINK_ON()
* STAY_ON()
* BLINK_OFF()
* DESTROY()
* debug()

 HUD_RADIO_STATIONS_WHEEL
^^^^^^^^^^^^^^^^^^^^^^^^^

* HUD_RADIO_STATIONS_WHEEL()
* INITIALISE(mc)
* clearStations()
* drawStations()
* SET_RADIO_STATIONS(params)
* SET_ADDITIONAL_RADIO_STATIONS(params)
* DRAW_RADIO_STATIONS()
* QUICK_SELECT_RADIO_STATION(params)
* SELECT_RADIO_STATION(params)
* SET_CURRENTLY_PLAYING(params)
* SET_AS_SHARED()
* hideShared()
* HIDE_CURRENTLY_PLAYING()
* SHOW()
* HIDE()
* HIDE_RADIO_STATIONS()
* REMOVE()

 HUD_RADIO_WHEEL
^^^^^^^^^^^^^^^^


 HUD_RETICLE
^^^^^^^^^^^^

* HUD_RETICLE()
* READY(id)
* LOAD_RETICLE()
* SET_RETICLE_TYPE_EXTERNAL(weaponID, hasAccuracyAnim, hasReticleData, hasCompass, isSniper)
* SET_RETICLE_TYPE(params)
* initSpreadComponents()
* SET_RETICLE_ACCURACY_EXTERNAL(accuracyScalar)
* SET_RETICLE_ACCURACY(params)
* SET_RETICLE_TEXT(params)
* SET_SCOPE_LOCK_EXTERNAL(isLocked, lockedStr)
* SET_SCOPE_LOCK(params)
* SET_SCOPE_DIST_EXTERNAL(distStr, feetStr)
* SET_SCOPE_DIST(params)
* SET_RETICLE_ZOOM_EXTERNAL(zoomLevel)
* SET_RETICLE_ZOOM(params)
* START_DIM_RETICLE_EXTERNAL(newAlpha)
* START_DIM_RETICLE(params)
* RESET_RETICLE_EXTERNAL()
* RESET_RETICLE()
* START_FLASHING_RETICLE_EXTERNAL(r, g, b, a)
* START_FLASHING_RETICLE(params)
* SET_RETICULE_COLOR(params)
* STOP_FLASHING_RETICLE()
* flashNewColour()
* flashDefaultColour()
* SET_RETICLE_VISIBLE_EXTERNAL(isVisible)
* SET_RETICLE_VISIBLE(params)
* SET_RETICLE_POSITION_EXTERNAL(newX, newY, aspectRatioMultiplier)
* SET_RETICLE_POSITION(params)
* SHOW_HITMARKER_EXTERNAL(hitmarkerFrame)
* SET_RETICULE_BOOST(params)
* SHOW_HITMARKER(params)
* SHOW_FRIENDLY_FIRE_EXTERNAL(reticleVis)
* SHOW_FRIENDLY_FIRE(params)
* SET_RETICLE_STYLE_EXTERNAL(myStyle)
* SET_RETICLE_STYLE(params)
* SET_RETICLE_LOCKON_TYPE_EXTERNAL(lockOnType)
* SET_RETICLE_LOCKON_TYPE(params)
* SET_CAM_HEADING_EXTERNAL(a)
* SET_CAM_HEADING(params)
* SHOW_SNIPER_HIT_EXTERNAL()
* SHOW_SNIPER_HIT()
* COORDS_TO_SCREEN(posX, posY, aspectRatioMultiplier)
* SET_USING_REMOTE_PLAY(params)
* SET_AIRCRAFT_HUD(params)
* OVERRIDE_HOMING_SCOPE(params)
* percFromRad(input)
* getDialAngle(minRot, maxRot, scale, isClockwise)
* REMOVE()

 HUD_SAVING
^^^^^^^^^^^

* HUD_SAVING()
* INITIALISE(mc)
* READY(id)
* SET_SAVING_TEXT_STANDALONE(iconEnum, saveStr)
* SET_SAVING_TEXT(params)
* SHOW()
* STAY_ON_SCREEN()
* HIDE_SAVING()
* REMOVE()

 HUD_STREET_NAME
^^^^^^^^^^^^^^^^

* HUD_STREET_NAME()
* READY(id)
* SET_STREET_NAME(newName)
* FORCE_SHOW(_forceShow)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_SUBTITLE_TEXT
^^^^^^^^^^^^^^^^^^

* HUD_SUBTITLE_TEXT()
* INITIALISE(mc)
* clearBlipLayer()
* SET_SUBTITLE_TEXT_CUTSCENE(params)
* SET_SUBTITLE_TEXT_RAW(params)
* CLEAR_SUBTITLE_TEXT()
* CLEAR_SUBTITLE_TEXT_NOW()
* REMOVE()
* parseForGamerTag(str, size, textField)

 HUD_SUBTITLE_TEXT_BIG
^^^^^^^^^^^^^^^^^^^^^^


 HUD_VEHICLE_NAME
^^^^^^^^^^^^^^^^^

* HUD_VEHICLE_NAME()
* READY(id)
* SET_VEHICLE_NAME(newName)
* FORCE_SHOW(_forceShow)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()

 HUD_WANTED_STARS
^^^^^^^^^^^^^^^^^

* HUD_WANTED_STARS()
* INITIALISE(mc)
* READY(id)
* SET_PLAYER_WANTED_LEVEL(params)
* STOP_FLASHING_WANTED_STARS()
* FLASH_WANTED_STARS(params)
* GetAndAdjustBlinkRate()
* STAY_ON_SCREEN()
* STAY_OFF_SCREEN()
* REMOVE()

 HUD_WEAPON_ICON
^^^^^^^^^^^^^^^^

* HUD_WEAPON_ICON()
* INITIALISE(mc)
* getTopCompOffset()
* getBottomCompOffset()
* READY(id)
* SET_WEAPONS_AND_AMMO_FOREVER(params)
* fadeInAndDoNothing()
* SHOW_GRENADE_DROP(params)
* SET_WEAPON_TIMER(params)
* setAmmoStateForGrenade(isStandard)
* SET_AMMO_COUNT(params)
* setTextFields(ammoCount, clipCount, clipSize)
* setAmmoIcon(ammoType)
* SET_PLAYER_WEAPON(params)
* SHOW()
* STAY_ON_SCREEN()
* HIDE()
* REMOVE()
* setAsActive()

 HUD_WEAPON_WHEEL
^^^^^^^^^^^^^^^^^

* HUD_WEAPON_WHEEL()
* INITIALISE(mc)
* dbg(str)
* UPDATE_DEBUG_3D_SETTINGS(params)
* READY(id)
* SET_INPUT_EVENT(params)
* SET_PARACHUTE_IS_VISIBLE(params)
* setSpecialAmmoMC(ammoMC, num)
* SET_ATTACHMENT_LABELS(params)
* setWeaponLabel(weaponData)
* setWeaponPaging(pageIndex, pageMax)
* setWeaponLabelAndPage()
* highlightWeapon()
* setSlotHighlight(i, slotMC, bHighlight)
* SET_PLAYER_WEAPON_WHEEL(params)
* loadWeapon(weaponData, slotTypeIndex)
* cycleWeapons(dir)
* TOGGLE_POINTER_AND_WEAPON_NAME_VISIBILITY(params)
* SET_POINTER(params)
* getScreenCoords(x, y)
* setHudWeaponWheelHash()
* getCurrentWeaponData()
* SHOW()
* START_CROSSFADE(params)
* fadeComplete()
* SHOW_ALL()
* CLEAR_PLAYER_WEAPON_WHEEL(params)
* UNLOAD_WEAPON_WHEEL()
* REMOVE()
* SET_WHEEL_IN_CAR_MODE(params)
* hideArrows()

 HUD_WEAPON_WHEEL_STATS
^^^^^^^^^^^^^^^^^^^^^^^

* HUD_WEAPON_WHEEL_STATS()
* INITIALISE(mc)
* dbg(str)
* UNLOAD_WEAPON_WHEEL_STATS()
* SHOW_ALL()
* REMOVE()
* DoBar(bar, base, attachment)
* SET_STATS_LABELS_AND_VALUES(params)
* CLEAR_STATS_LABELS_AND_VALUES()
* SET_STATS_VISIBILITY(params)

 IAA_HEIST_BOARD
^^^^^^^^^^^^^^^^

* IAA_HEIST_BOARD()
* initialise(mc)
* TXD_HAS_LOADED(txd, success, id)
* SET_INPUT_EVENT(inputID)
* ENABLE_NAVIGATION()
* DISABLE_NAVIGATION()
* SET_CURRENT_SELECTION(id)
* GET_CURRENT_SELECTION()
* SET_ACTIVE_ITEM_SELECTED(isSelected)
* SHOW_LOADING()
* SHOW_SETUP(skipLoader, title, gangName, description)
* SHOW_REPLAY(skipLoader, title, gangName)
* SHOW_LAUNCH(skipLoader, title, gangName, missionName, description, cost, texture, txd)
* SHOW_FINALE(skipLoader, title, gangName, isLeader)
* SET_MAP_DISPLAY(x, y, scale, cutToPosition)
* ADD_MAP_MARKER(id, x, y, label)
* REMOVE_MAP_MARKER(id)
* RESET_MAP()
* FLASH_ACTIVE_ELEMENT()
* PULSE_ELEMENT(elementID)
* SET_SPY_CAM_TEXTURES(txd, topTexture, leftTexture1, leftTexture2, leftTexture3, leftTexture4, leftTexture5, rightTexture1, rightTexture2, rightTexture3, bottomTexture)
* SET_SETUP_MISSION(index, prep1Title, prep1Description, prep1State, prep1Texture, prep2Title, prep2Description, prep2State, prep2Texture, finalTitle, finalDescription, finalState, finalTexture, lockedMessage, prep1Stat, prep2Stat, finalStat, txd)
* SET_REPLAY_MISSION(index, title, description, cost, texture, isUnavailable, txd)
* SET_FINALE_PLAYER(index, gamertag, headshotTexture, isLocalPlayer)
* REMOVE_FINALE_PLAYER(index)
* UPDATE_FINALE_PLAYER_ROLE(index, role)
* UPDATE_FINALE_PLAYER_STATUS(index, isReady)
* UPDATE_CASH_DISTRIBUTION(player0Cash, player1Cash, player2Cash, player3Cash, unassignedCash)
* SET_LAUNCH_STATE(enabled, hidden)
* UPDATE_FINALE_PLAN()
* clearUI()
* initSetupNavigation()
* updateSetupNavigation()
* onSetupNavigationChange(activeElementID)
* initLaunchNavigation()
* initReplayNavigation()
* updateReplayNavigation()
* onReplayNavigationChange(activeElementID)
* updateFinaleView()
* initFinaleNavigation(isLeader)
* updateFinaleNavigation()
* onFinaleNavigationChange(activeElementID)
* delegate(scope, method)
* setLocalisedText(tf, label)
* setEllipsis(label, tf)

 IMPORT_EXPORT_WAREHOUSE
^^^^^^^^^^^^^^^^^^^^^^^^

* IMPORT_EXPORT_WAREHOUSE()
* initialise(mc)
* debugCalls()
* ACTIVATE()
* DEACTIVATE()
* SHOW_EXPORT_SCREEN()
* UPDATE_VEHICLE(id, value, collectionValue, selected, owned, rangeCategory, actualValue)
* UPDATE_COLLECTION(id, value, selected, disabled)
* SHOW_BUYERS(buyerRequirement0, buyerRequirement1, buyerRequirement2, buyerValue0, buyerValue1, buyerValue2, buyer0Available, buyer1Available, buyer2Available)
* SET_COOLDOWN(cooldownSeconds)
* SHOW_OVERLAY(titleLabel, messageLabel, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_TAB_ID()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* TXD_HAS_LOADED(txd, success, id)
* getVehicleById(id)
* getCollectionFromStaticDataById(id)
* createVehicleClasses()

 JOB_LIST
^^^^^^^^^

* JOB_LIST()
* construct()
* populateContent()
* setState(item, isActive)
* setupJob(selected)
* parseForGamerName(TF, str)

 LESTER_HACK_PC
^^^^^^^^^^^^^^^

* LESTER_HACK_PC()
* INITIALISE(mc)
* SHOW_IFINDER_POPUP()
* HIDE_IFINDER_POPUP()

 LETTER_SCRAPS
^^^^^^^^^^^^^^

* LETTER_SCRAPS()
* INITIALISE(mc)
* SET_LETTER_TEXT(str)
* ADD_TO_LETTER_TEXT(str)
* SET_BG_VISIBILITY(value)

 MARKER
^^^^^^^


 MARKER_LEFT
^^^^^^^^^^^^


 MARKER_RIGHT
^^^^^^^^^^^^^


 MESSAGE_LIST
^^^^^^^^^^^^^

* MESSAGE_LIST()
* construct()
* populateContent()
* setState(item, isActive)
* parseForGamerName(TF, str)

 MESSAGE_VIEW
^^^^^^^^^^^^^

* MESSAGE_VIEW()
* construct()
* populateContent()
* setupMessageBody()
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* LOADCLIP(textureDict, targetMC)
* onLoadInit(target_mc)
* CLEAN_UP_DATA()

 MIDSIZED_MESSAGE
^^^^^^^^^^^^^^^^^

* MIDSIZED_MESSAGE()
* INITIALISE(mc)
* SHOW_MIDSIZED_MESSAGE(title, description)
* SHOW_BRIDGES_KNIVES_PROGRESS(title, totalToDo, message, info, completed)
* SHOW_COND_SHARD_MESSAGE(bigText, msgText, colID, useDarkerShard)
* SHOW_SHARD_MIDSIZED_MESSAGE(bigText, msgText, colID, useDarkerShard, useCondensedShard)
* SHARD_SET_TEXT(bigText, msgText, useCondensedShard)
* SHARD_ANIM_OUT(colID, animTime)
* parseForGamerTagTitleFonts(tf, str, stdPtSize)
* getFontSizeFit(gamerName, fontSize, widthToFit)

 MISSION_COMPLETE
^^^^^^^^^^^^^^^^^

* MISSION_COMPLETE()
* INITIALISE(mc)
* SET_DATA_SLOT(_slotIndex)
* UPDATE_DATA_SLOT(_slotIndex)
* DRAW_MENU_LIST()
* HIGHLIGHT_ITEM(i, highlight)
* SET_MISSION_TITLE_COLOUR(r, g, b)
* SET_MISSION_SUBTITLE_COLOUR(r, g, b)
* SET_MISSION_BG_COLOUR(r, g, b)
* clampText(textF, labelS, maxVal)
* SET_MISSION_TITLE(title, desc)
* SET_TOTAL(medalID, totalValue, totalLabel)
* SET_MEDAL(medalID)
* animateIn()
* animateInComplete()
* resizeBackground()

 MISSION_QUIT
^^^^^^^^^^^^^

* MISSION_QUIT()
* INITIALISE(mc)
* SET_TEXT(title, copy)
* TRANSITION_IN(duration)
* TRANSITION_OUT(duration)
* _handleTransitionOutComplete()

 MISSION_REPEAT_LIST
^^^^^^^^^^^^^^^^^^^^

* MISSION_REPEAT_LIST()
* construct()
* populateContent()
* setState(item, isActive)

 MISSION_TARGET_COMPLETE
^^^^^^^^^^^^^^^^^^^^^^^^

* MISSION_TARGET_COMPLETE()
* INITIALISE(mc)
* SET_DATA_SLOT()
* clampText(textF, labelS, maxVal)
* SHOW(_fadeTime)
* onShow()
* HIDE(_fadeTime)

 MORGUE_LAPTOP
^^^^^^^^^^^^^^

* MORGUE_LAPTOP()
* initialise(mc)
* SET_PROGRESS_PERCENT(percent)

 MP_AWARD_BASE
^^^^^^^^^^^^^^

* MP_AWARD_BASE()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef)
* INITIALISE(mc, fileName)
* loadComponent(txd, texture)
* SHOW_AWARD_AND_MESSAGE(awTitle, awDesc, txd, texture, awDesc2, colEnum)
* SHOW_UNLOCK_AND_MESSAGE(awTitle, awDesc, txd, texture, awDesc2, colEnum)
* ADD_TXD_REF_RESPONSE(textureDict, success)
* OVERRIDE_Y_POSITION(newYPosition)
* debug()

 MP_AWARD_FREEMODE
^^^^^^^^^^^^^^^^^^

* MP_AWARD_FREEMODE()
* INITIALISE(mc, fileName)
* RESET_AWARDS_MOVIE()
* loadComponent(txd, texture)
* SHOW_AWARD_AND_MESSAGE(awTitle, awDesc, txd, texture, awDesc2, colEnum, awDesc3)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueStr, success)
* debug()

 MP_BIG_MESSAGE_FREEMODE
^^^^^^^^^^^^^^^^^^^^^^^^

* MP_BIG_MESSAGE_FREEMODE()
* INITIALISE(mc)
* createMessageNG(linkageID, args)
* SET_SHARD_BACKGROUND_TARGET_HEIGHT(numStats)
* SET_SHARD_BACKGROUND_HEIGHT(height)
* ROLL_DOWN_BACKGROUND()
* ROLL_UP_BACKGROUND()
* UPDATE_MESSAGE(msgText)
* createMessage(linkageID, args)
* setBigMessageOutline(bigTextStr)
* SET_RESPAWN_BAR_PERCENTAGE(precent)
* FLASH_RESPAWN_BAR(duration)
* UPDATE_STRAP_MESSAGE(msgText)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* CLEAR_CREW_RANKUP_MP_MESSAGE()
* SHOW_BUSTED_MP_MESSAGE()
* SHOW_WASTED_MP_MESSAGE()
* SHOW_RANKUP_MP_MESSAGE(bigText)
* SHOW_CREW_RANKUP_MP_MESSAGE(titleStr, msgStr, rankNumber, emblemTXD, emblemTXN, alpha)
* SHOW_LOCKED_UP_MP_MESSAGE()
* SHOW_MISSION_END_MP_MESSAGE()
* SHOW_MISSION_FAILED_MP_MESSAGE()
* SHOW_MISSION_PASSED_MESSAGE()
* SHOW_WEAPON_PURCHASED(bigMessage, weaponName, weaponHash, weaponDescription, alpha)
* SHOW_PLANE_MESSAGE(bigMessage, planeName, planeHash)
* SHOW_TERRITORY_CHANGE_MP_MESSAGE()
* SHOW_MP_MESSAGE_TOP()
* SHOW_CENTERED_MP_MESSAGE_LARGE()
* SHOW_CENTERED_MP_MESSAGE()
* SHOW_CENTERED_TOP_MP_MESSAGE()
* SHOW_BIG_MP_MESSAGE_WITH_STRAP_AND_RANK()
* SHOW_BIG_MP_MESSAGE_WITH_STRAP()
* SHOW_BIG_MP_MESSAGE()
* SHOW_SHARD_CENTERED_MP_MESSAGE()
* SHOW_SHARD_CENTERED_MP_MESSAGE_LARGE()
* SHOW_SHARD_WASTED_MP_MESSAGE(bigTxt, msgTxt, colId, someUnusedBoolean, darkenBackground)
* SHOW_SHARD_CENTERED_TOP_MP_MESSAGE()
* SHOW_SHARD_RANKUP_MP_MESSAGE()
* SHOW_SHARD_CREW_RANKUP_MP_MESSAGE()
* DO_SHARD(args, isCenter, colID, shardColID, useLargeShard)
* getFontSizeFit(gamerName, fontSize, widthToFit)
* parseForGamerTagTitleFonts(tf, str, stdPtSize)
* colourSwitch()
* colourSwitchAnim()
* SHARD_SET_TEXT(bigText, msgText, colID)
* SHARD_ANIM_DELAY(delayTime)
* SHARD_ANIM_OUT(colID, animTime, textColourId)
* SET_RANK_ICON_RGB(r, g, b)
* playIconAnimation(iconText)
* TRANSITION_OUT(duration)
* getStringSize(str)
* RESET_MOVIE()
* OVERRIDE_Y_POSITION(newYPosition)
* TRANSITION_IN(duration)
* TRANSITION_UP(duration, preventAutoExpansion)
* showMessageAfterTransitionUp()
* TRANSITION_DOWN(duration)
* showStrapMessage()
* transitionUpComplete()
* saveStrapStateOnAnimate()
* debug()

 MP_BOUNTY_BOARD
^^^^^^^^^^^^^^^^

* MP_BOUNTY_BOARD()
* INITIALISE(mc)
* SET_BOUNTY(bountysName, bountValue, bountyCharacterTexture, bountyCharacterDictionary)
* loadComponent(txd, texture)
* TXD_HAS_LOADED(textureDict, success)

 MP_CAR_STATS
^^^^^^^^^^^^^

* MP_CAR_STATS()
* INITIALISE(mc, fileName)
* SET_VEHICLE_INFOR_AND_STATS(vehicleInfo, vehicleDetails, logoTXD, logoTexture, statStr1, statStr2, statStr3, statStr4, statVal1, statVal2, statVal3, statVal4)
* setBars(barID, percentage)
* TXD_HAS_LOADED(textureDict, success)
* loadTexture(txd, texture)
* debug()

 MP_CELEBRATION
^^^^^^^^^^^^^^^

* MP_CELEBRATION()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef)
* INITIALISE(mc, type)
* SET_GFX_TYPE(type)
* SET_CUSTOM_SOUND(id, sound, soundSet)
* CREATE_STAT_WALL(id, colourName, fgAlpha)
* ADD_BREAKPOINT(wallId)
* RESUME_FROM_BREAKPOINT(wallId)
* SET_PAUSE_DURATION(duration)
* SHOW_STAT_WALL(wallId)
* PAUSE_BEFORE_PREVIOUS_LAYOUT(wallId, duration)
* PAUSE(wallId, duration)
* UNPAUSE(wallId)
* OVERRIDE_PAUSES(wallId, ignore)
* GET_TOTAL_WALL_DURATION()
* doNextAnimation(wallId, firstRun)
* drawFinalVerticalFlag(bg, wallObject)
* syncBeforeNextAnimation(wallId)
* backgroundTweenInComplete(bg)
* drawStaticVerticalFlag(bg)
* backgroundTweenOutComplete()
* SHOW_FLASH(inDuration, holdDuration, outDuration, colourName)
* fadeAndRemoveMc(mc, duration, delay)
* CLEANUP(wallId)
* ADD_BACKGROUND_TO_WALL(wallId, alpha, textureId)
* drawStartingVerticalFlag(mc, wallObject)
* ADD_SCORE_TO_WALL(wallId, textLabel, score)
* getAvailableTextWidth(tf, belowText, rightToLeft, limit)
* ADD_POSITION_TO_WALL(wallId, position, positionLabel, isPositionLabelRawText, isScore)
* ADD_JOB_POINTS_TO_WALL(wallId, points, xAlign)
* ADD_ARENA_POINTS_TO_WALL(wallId, points, xAlign)
* ADD_POINTS_TO_WALL(wallId, points, type, prefix, xAlign, marginTop, noAnims)
* ADD_REP_POINTS_AND_RANK_BAR_TO_WALL(wallId, repPointsGained, startRepPoints, minRepPointsForRank, maxRepPointsForRank, currentRank, nextRank, rank1Txt, rank2Txt)
* addPointsAndRankBarToWall(wallId, repPointsGained, startRepPoints, minRepPointsForRank, maxRepPointsForRank, currentRank, nextRank, rank1Txt, rank2Txt, iconNum, rankBGIcon)
* ADD_ARENA_POINTS_AND_RANK_BAR_TO_WALL(wallId, repPointsGained, startRepPoints, minRepPointsForRank, maxRepPointsForRank, currentRank, nextRank, rank1Txt, rank2Txt)
* showRankUp(layoutMc, currentRank, nextRank)
* completeRankUpAnimation(layoutMc, nextRank)
* completeRankUpAnimationGlobe(layoutMc, nextRank)
* ADD_WINNER_TO_WALL(wallId, winLoseTextLabel, gamerName, crewName, betAmount, isInFlow, teamName, gamerNameIsLabel)
* ADD_OBJECTIVE_TO_WALL(wallId, objectiveTitleLabel, objectiveText, isObjectiveTitleRawText)
* ADD_ARENA_UNLOCK_TO_WALL(wallId, objectiveTitleLabel, objectiveText, isObjectiveTitleRawText)
* ADD_MISSION_RESULT_TO_WALL(wallId, missionTextLabel, passFailTextLabel, missionReasonString, isReasonRawText, isPassFailRawText, isMissionTextRawText, forcedAlpha, hudColourId)
* ADD_TIME_TO_WALL(wallId, time, timeTitleLabel, timeDifference)
* ADD_CHALLENGE_SET_TO_WALL(wallId, score, time, setTextLabel, challengeName, alpha)
* ADD_STAT_NUMERIC_TO_WALL(wallId, statLabel, statValue, xAlign, isRawText)
* ADD_CASH_WON_TO_WALL(wallId, statLabel, statValue, potentialValue, xAlign, isRawText)
* CREATE_INCREMENTAL_CASH_ANIMATION(wallId, animationId)
* ADD_INCREMENTAL_CASH_WON_STEP(wallId, animationId, startingValue, finishingValue, topText, bottomText, rightHandStat, rightHandIcon)
* ADD_INCREMENTAL_CASH_ANIMATION_TO_WALL(wallId, animationId)
* incrementCashAnimation(stepData, animation, cashMC, prevCashMC)
* ADD_WAVE_REACHED_TO_WALL(wallId, waveText, reachedLabel)
* ADD_WORLD_RECORD_TO_WALL(wallId, time)
* ADD_TOURNAMENT_TO_WALL(wallId, playlistName, qualificationLabel, resultText, isResultTextRawText, resultValue)
* ADD_INTRO_TO_WALL(wallId, modeLabel, jobName, challengeTextLabel, challengePartsText, targetTypeTextLabel, targetValue, delay, targetValuePrefix, modeLabelIsStringLiteral, textColourName)
* ADD_READY_TO_WALL(wallId, readyLabel)
* ADD_CASH_TO_WALL(wallId, cashAmount, xAlign)
* ADD_POST_UNLOCK_CASH_TO_WALL(wallId, cashAmount, xAlign)
* ADD_CHALLENGE_PART_TO_WALL(wallId, winLoseTextLabel, challengePartsText)
* CREATE_STAT_TABLE(wallId, tableId)
* ADD_STAT_TO_TABLE(wallId, tableId, statText, statValue, isStatTextRawText, isStatValueRawText, isTotalRow, isStatValueTime, colour)
* ADD_STAT_TABLE_TO_WALL(wallId, tableId)
* ADD_CHALLENGE_WINNER_TO_WALL(wallId, challengeTextLabel, winLoseTextLabel, crewName, challengeName, cashAmount, isInFlow, isWinner, isMission, isWinLoseTextLabelRawText, teamName)
* toggleVisibility(mcs, delay, parentMc)
* processTextField(tf, format, props)
* doCentralisedTextLayout(centralTf, topLeftTfs, topRightTfs, bottomLeftTfs, bottomRightTfs, maxWidth, maxHeight)
* createLayoutMc(wallId, layoutId, layoutName)
* addAnimationsToWall(wallId, targetY, offsetY, childAnims, delay, duration, pauseBefore, soundName, soundSet)
* addMcToWall(wallId, mc, mcHeight, mcTopPadding, xAlign, xOffset, vAlign)
* processMcsForGfxType(mcs)
* getMovieClipFromName(mcName)
* getObjectFromMcName(mcName)
* stringInArray(input, what)
* getColour(col)
* getAlignment(align)
* doNumericTween(tf, startNumber, targetNumber, duration, delay)
* startCounter(tf, startNumber, delta, duration)
* updateCounter(tf, startNumber, delta, startTimestamp, duration)
* playSound(soundName, libName)
* formatTimeMs(ms)
* zeroPadNumberString(number, width)
* syncPointReached(syncClearCallback)
* registerSyncedMovie(sequenceTypeBit)
* syncPointClear()
* createDelegate(scope, method)

 MP_CORONA_PLAYER_INFO
^^^^^^^^^^^^^^^^^^^^^^

* MP_CORONA_PLAYER_INFO()
* INITIALISE(mc)
* SHOW_COLUMN(bool)
* setColumnDependent(columnMC)
* DISPLAY_VIEW(viewIndex, itemIndex)
* UPDATE_SLOT(_viewIndex, _slotIndex)
* onDisplayUpdate()
* checkForCollisions()
* checkCollisionAgainst(itemMC)

 MP_CREW_TAG
^^^^^^^^^^^^

* MP_CREW_TAG()
* INITIALISE(mc)
* SET_CREW_TAG(crewTypeIsPrivate, crewTagContainsRockstar, crewTag, founderOrRank)
* debug()

 MP_FREEMODE_CHECKPOINT_BASE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* MP_FREEMODE_CHECKPOINT_BASE()
* INITIALISE(mc)
* SET_CHECKPOINT_TEXT(str)

 MP_FREEMODE_PLAYER_LIST
^^^^^^^^^^^^^^^^^^^^^^^^

* MP_FREEMODE_PLAYER_LIST()
* INITIALISE(mc)
* REORDER()
* repositionInOrder()
* REMOVE_FROM_SESSION_BY_ID(id)
* SET_TIME_BY_ID(id, time)
* SET_ICON(index, iconEnum, rank)
* SET_ITEM_TEXT_RIGHT(id, str)
* DISPLAY_MIC()
* SET_TITLE(str)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* COLLAPSE(collapse)
* SET_ROW_SPACING(_rowSpacing)
* SET_DESCRIPTION(cashStr, totalBetsStr, betsOnYouStr, helpStr)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_HIGHLIGHT(i)
* SET_INPUT_EVENT(direction)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* ON_DESTROY()

 MP_GAMER_INFO
^^^^^^^^^^^^^^

* MP_GAMER_INFO()
* SET_GAMERNAME_AND_PACKED_CREW_TAG(gamerName, crewTag)
* debug()

 MP_MATCHMAKING_CARD
^^^^^^^^^^^^^^^^^^^^

* MP_MATCHMAKING_CARD()
* INITIALISE(mc)
* SET_TITLE(str, verified)
* SET_ICON(index, iconEnum, rank)
* DISPLAY_MIC()
* COLLAPSE(collapse)
* SET_ROW_SPACING(_rowSpacing)
* SET_DESCRIPTION(cashStr, totalBetsStr, betsOnYouStr, helpStr)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_HIGHLIGHT(i)
* SET_STATE(i, _txdLevelOverride)
* SET_INPUT_EVENT(direction)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* ON_DESTROY()

 MP_MATCHMAKING_SELECTOR
^^^^^^^^^^^^^^^^^^^^^^^^

* MP_MATCHMAKING_SELECTOR()
* INITIALISE(mc)
* SHOW_GAMER_INFO(colIndex, name, crewName, crewTagStr, txd, txn)
* SHOW_CENTER_CONTENT(show)
* SHOW_BOTTOM_SELECTOR(show)
* SHOW_LEFT_ARROW(show)
* SHOW_RIGHT_ARROW(show)
* SHOW_UP_DOWN_ARROWS(show)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID)
* SHOW_BET_SELECTOR(betsOnVal, oddsVal, myBetVal)
* SET_BETS_ON_PLAYER(val)
* LOCK_BETTING(locked)
* SET_ODDS(val)
* SET_MY_BET(val)
* SHOW_VEHICLE_SELECTOR(name, type, colour, colourType)
* SHOW_QUESTION_MARK(show)
* SET_VEHICLE_NAME(name)
* SET_VEHICLE_TYPE(type)
* SET_COLOUR(colour)
* SET_COLOUR_TYPE(colourType)

 MP_MATCHMAKING_VEHICLE_INFO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* MP_MATCHMAKING_VEHICLE_INFO()
* INITIALISE(mc)
* SET_TITLE(nameStr, classStr)
* SET_DESCRIPTION(statusStr)
* imageLoaded()
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* resizeBG()

 MP_MENU_GLARE
^^^^^^^^^^^^^^

* MP_MENU_GLARE()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SET_DATA_SLOT(angle, triggerGlintAni)
* _updateDisplay()

 MP_MISSION_NAME_FREEMODE
^^^^^^^^^^^^^^^^^^^^^^^^^

* MP_MISSION_NAME_FREEMODE()
* INITIALISE(mc)
* SET_MISSION_INFO(missionName, missionType, playerInfo, percentage, debugValue, isRockstarVerified, playersRequired, RP, cash, time)
* setupCashAndRP(RP, cash)
* calcMissionNameSize(str)
* centreInformation(hasName, mc)
* debug()

 MP_MM_CARD_FREEMODE
^^^^^^^^^^^^^^^^^^^^

* MP_MM_CARD_FREEMODE()
* INITIALISE(mc)
* debug()
* COLLAPSE(collapse)
* SET_ICON(index, iconEnum, rank)
* DISPLAY_MIC()
* SET_TITLE(str, str2, icon)
* SET_DATA_SLOT(_viewIndex)
* UPDATE_SLOT(_viewIndex)
* SET_HIGHLIGHT(index)
* DISPLAY_VIEW()
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)

 MP_NEXT_JOB_SELECTION
^^^^^^^^^^^^^^^^^^^^^^

* MP_NEXT_JOB_SELECTION()
* INITIALISE(mc)
* SET_TITLE(sTitle, sVotes)
* SHOW_PLAYER_VOTE(i, sGamerName, r, g, b)
* SET_GRID_ITEM(i, sTitle, sTXD, sTXN, textureLoadType, verifiedType, eIcon, bCheck, rpMult, cashMult, bDisabled, iconCol, apMult)
* SET_GRID_ITEM_VOTE(i, iNumVotes, voteBGColour, bShowCheckMark, bFlashBG)
* SET_SELECTION(i, sTitle, sDetails, bHideHighlight)
* SET_HOVER(itemIndex, hideHover)
* SET_DETAILS_ITEM(detailIndex)
* TXD_HAS_LOADED(sTXD, success, uID)
* TXD_ALREADY_LOADED(sTXD, uID)
* ADD_TXD_REF_RESPONSE(sTXD, uID, success)
* SET_LOBBY_LIST_VISIBILITY(bShowList)
* SET_LOBBY_LIST_DATA_SLOT()
* UPDATE_LOBBY_LIST_DATA_SLOT()
* DISPLAY_LOBBY_LIST_VIEW()
* SET_LOBBY_LIST_HIGHLIGHT()
* SET_LOBBY_LIST_DATA_SLOT_EMPTY()
* INIT_LOBBY_LIST_SCROLL()
* SET_LOBBY_LIST_SCROLL()
* CLEANUP_MOVIE()
* SET_ITEMS_GREYED_OUT(value)

 MP_PLAYER_CARD
^^^^^^^^^^^^^^^

* MP_PLAYER_CARD()
* DISPLAY_VIEW()
* INITIALISE(mc, collapse)
* SET_TITLE(title)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_DESCRIPTION(descStr, descType, crewTagStr)
* SET_DATA_SLOT_EMPTY()

 MP_RANK_BAR
^^^^^^^^^^^^

* MP_RANK_BAR()
* INITIALISE()
* READY(id)
* RESET_MOVIE()
* SET_COLOUR(params)
* OVERRIDE_ANIMATION_SPEED(params)
* OVERRIDE_ONSCREEN_DURATION(params)
* SET_BAR_TEXT(params)
* RESET_BAR_TEXT()
* SET_RANK_SCORES(params)
* animatateScores(currentRankLimit, nextRankLimit, playersPreviousXP, playersCurrentXP, rank, rankNext)
* animateRankUp(rank)
* animateRankNumbersIn(rank)
* animateRankNumbersOut(rank)
* getRankFrame(_rankValue)
* tickUnderRank()
* calcIncrement(difBetweenRanks)
* checkQueuedItems()
* SHOW()
* STAY_ON_SCREEN()
* FADE_BAR_OUT(params)
* HIDE()
* REMOVE()
* debug()

 MP_RESULTS_PANEL
^^^^^^^^^^^^^^^^^

* MP_RESULTS_PANEL()
* INITIALISE(mc)
* initScreenLayout()
* SET_TITLE(title)
* SET_SUBTITLE(label)
* SET_SLOT(id, state, label)
* SET_SLOT_STATE(id, state)
* CLEAR_SLOT(id)
* CLEAR_ALL_SLOTS()
* updateDisplay()
* ApplyHudColourToTF(tf, colourId)

 MP_SPECTATOR_CARD
^^^^^^^^^^^^^^^^^^

* MP_SPECTATOR_CARD()
* INITIALISE(mc)
* createPool(num)
* START_NEW_ORDER()
* ADD_NEW_ORDER_ITEM(index)
* END_NEW_ORDER()
* removefromList()
* addToList()
* setTopEdge(oldLen)
* scrollFeild()
* setPoolItemActive(poolItem, bool)
* getItemFromPool()
* SET_ICON(index, iconEnum, rank)
* DISPLAY_MIC()
* SET_ITEM_TEXT_RIGHT(id, str)
* SET_TITLE(str)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* COLLAPSE(collapse)
* SET_DESCRIPTION(cashStr, totalBetsStr, betsOnYouStr, helpStr)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_HIGHLIGHT(_highlightIndex)
* REORDER()
* REMOVE_FROM_SESSION_BY_ID(id)
* SET_TIME_BY_ID(id, time)

 MP_SPECTATOR_OVERLAY
^^^^^^^^^^^^^^^^^^^^^

* MP_SPECTATOR_OVERLAY()
* INITIALISE(mc)
* debug()
* update()
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SHOW_TICKER(value)
* SHOW_POSITIONS(value)
* SET_TITLE(missionType, missionName, missionDesc)
* SET_NEXT_TITLE(missionType, missionName, missionDesc)
* ANIM_NEXT_TITLE_IN()
* ANIM_NEXT_TITLE_OUT()
* ANIM_NEXT_TITLE()
* ADD_FEED_TEXT()
* ADD_JOB_TEXT()
* INIT_SCORE()
* SET_PLAYER_SCORE(index, show, position, gamertag, score)
* _positionPositionsPanel()
* _positionLowerThird()
* _howWide(target)

 MP_UNLOCKS_FREEMODE
^^^^^^^^^^^^^^^^^^^^

* MP_UNLOCKS_FREEMODE()
* INITIALISE(mc, fileName)
* RESET_AWARDS_MOVIE()
* SHOW_UNLOCK_AND_MESSAGE(awTitle, awDesc, txd, texture, awDesc2, colEnum)
* SHOW_COLLECTION_PROGRESS(title, completed, totalToDo, message, info)
* SHOW_BRIDGES_KNIVES_PROGRESS(title, totalToDo, message, info, completed)
* debug()

 MUGSHOT_BOARD
^^^^^^^^^^^^^^

* MUGSHOT_BOARD()
* INITIALISE(mc)
* SET_BOARD(headerStr, numStr, footerStr, importedStr, importCol, rankNum, rankCol)

 MULTIPLAYER_CHAT
^^^^^^^^^^^^^^^^^

* MULTIPLAYER_CHAT()
* INITIALISE(mc)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept)
* initGameFeed()
* initLobbyFeed()
* initTextInput()
* hide()
* showInput(scope, eHudColour)
* showFeed()
* historyUp()
* historyDown(forceFinishTweens)
* ADD_TEXT(text)
* DELETE_TEXT()
* ABORT_TEXT()
* COMPLETE_TEXT()
* SET_TYPING_DONE()
* ADD_MESSAGE(player, message, scope, teamOnly, eHudColour)
* SET_FOCUS(eVisibleState, scopeType, scope, player, eHudColour)
* SET_FOCUS_MODE(focusMode)
* PAGE_UP()
* PAGE_DOWN()
* RESET()

 NEW_EDITOR
^^^^^^^^^^^

* NEW_EDITOR()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* INITIALISE(mc)
* SET_MOVIE_MODE(movieMode)
* showProjectSizeWidget(showWidget)
* setup()
* SET_HEADER_VISIBLE(isVisible)
* SET_CLIP_EDIT_HEADER_VISIBLE(isVisible)
* debug()
* SET_CLIP_EDIT_HEADER(strL, strR)
* SET_PAGE_HEADING(pageHeading)
* SET_PAGE_HEADING_RIGHT(pageHeading)
* BEGIN_ADDING_COLUMN_DATA(columnId, columnTpye, colTitle)
* END_ADDING_COLUMN_DATA(shouldRender, beActive)
* ADD_COLUMN_ITEM_INACTIVE()
* ADD_COLUMN_ITEM()
* ADD_COLUMN_ITEM_WITH_OPTIONS()
* ADD_COLUMN_ITEM_WITH_TWO_STRINGS()
* ADD_COLUMN_ITEM_WITH_ICON()
* ADD_COLUMN_HELP_TEXT()
* ADD_COLUMN_HEADER()
* ADD_COLUMN_HEADER_WITH_TWO_STRINGS()
* ADD_PROJECT_SIZE_DISPLAY()
* ADD_LIST_SCROLL_ITEM(label)
* UPDATE_SCROLL_LIST_LABEL(label)
* UPDATE_LIST_ITEM(colID, itemID)
* SET_ICON_VISIBILITY_FROM_LIST_ITEM(colID, itemID, isVisible)
* UPDATE_LIST_ITEM_ELEMENT(colID, itemID, elementID, elementData)
* UPDATE_COLUMN_HELP_TEXT(helpTextData)
* UPDATE_COLUMN_PROJECT_SIZE(value)
* UPDATE_COLUMN_PROJECT_SIZE_TITLE(titleTextData)
* UPDATE_COLUMN_PROJECT_SIZE_X_POSITION(xPos)
* UPDATE_UPLOAD_PROCESS(label)
* UPDATE_UPLOAD_BACKGROUND(stateId)
* SET_ANIMATED_AUDIO_ICON(itemId, isPlaying)
* BUILD_MENU()
* GO_TO_NEXT_ITEM()
* GO_TO_PREVIOUS_ITEM()
* SET_ITEM_ACTIVE(colID, itemID)
* UNSET_ITEM_ACTIVE()
* SET_ITEM_SELECTED(itemId, onlyOneOption)
* SET_COL_TYPE_LIST_COLOUR(itemId, stateId)
* SET_COL_TYPE_LIST_COLOUR_IN_COLUMN(colId, itemId, stateId)
* SET_COLUMN_ACTIVE(colID)
* GET_ACTIVE_ITEM()
* GO_TO_NEXT_COLUMN()
* GO_TO_PREVIOUS_COLUMN()
* REMOVE_COLUMN(columnId)
* UNHIGHLIGHT()
* SET_ITEMS_GREYED_OUT(itemID)
* SET_ITEMS_UNGREYED_OUT(itemID)
* HIGHLIGHT_ITEM(itemID)
* createColumn(columnId, colTpye)
* tabFrameFromColType(colType)
* registerMovie(mc)
* unRegister(mc)
* SET_PLAYBACK_MENU_VISIBLE(isVisible)
* initColourGrabbing()

 NEW_HUD
^^^^^^^^

* NEW_HUD()
* SET_CHARACTER_COLOUR(colourEnum)
* SET_WEAPON_WHEEL_ACTIVE(bool)
* GET_CURRENT_WEAPON_WHEEL_HASH()
* SET_CURRENT_WEAPON_WHEEL_HASH(newWeaponHash, isWeaponSelectable)
* setupComponent(componentID)
* setAllHudIntendedVisibility(isVisible)
* SHOW(componentID)
* HIDE(componentID)
* SHOW_ALL()
* HIDE_ALL()
* REMOVE_HUD_ITEM(componentID, wasCalledFromCode)
* addObjectToList(componentID, listID, rowPriority)
* reorderAllKnownLists()
* reorderList(listID)
* createComponentMovieClip(currentComp)

 NIGHTCLUB
^^^^^^^^^^

* NIGHTCLUB()
* initialise(mc)
* SET_GENERAL_STATS(gamerName, propertyDictionary, propertyTexture, clubNameID, propertyLocation, organizationType, organizationName, popularity, totalStockValue, mugshotTexture, clubStyle)
* SET_HOMEPAGE_STATS(jobsCompleted, nightclubEarnings, salesCompleted, warehouseEarnings, totalEarnings)
* SET_NIGHTCLUB_STATS(currentCustomers, averageCustomers, dailyIncome, safeCurrent, safeCapacity, vipAppearances, dayGraphMon, dayGraphTue, dayGraphWed, dayGraphThu, dayGraphFri, dayGraphSat, dayGraphSun, dayGraphMax)
* UPDATE_MANAGEMENT_COOLDOWN(managementCooldown)
* SET_WAREHOUSE_STATS(unitsAccrued, unitsSold, unitsAvailable)
* UPDATE_DJ(index, state, dummy, name, unused, cost, saleCost, textureDictionary, texture, isMale, isSolo)
* UPDATE_STOCK(index, currLevel, maxLevel, sellPrice)
* UPDATE_TECHNICIAN(index, assignmentIndex, isAvailable, isOnSale)
* SELECT_TECHNICIAN(index)
* UPDATE_ASSIGNMENT(index, available, isAtCapacity)
* UPDATE_UPGRADE(index, cost, saleCost, availability)
* UPDATE_BUYER(index, name, price, cargoType0, cargoAmount0, cargoType1, cargoAmount1, cargoType2, cargoAmount2)
* UPDATE_SELL_COOLDOWN(sellCooldown)
* SET_AUDIO_BUTTON(index, isPlaying)
* RESET_AUDIO_BUTTONS()
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* GET_CURRENT_ROLLOVER()
* GET_CURRENT_SCREEN_ID()
* IS_HISTORY_EMPTY()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)

 OBSERVATORY_SCOPE
^^^^^^^^^^^^^^^^^^

* OBSERVATORY_SCOPE()
* INITIALISE(mc)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* initScreenLayout()

 OPEN_WHEEL_HEALTH_INDICATOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* OPEN_WHEEL_HEALTH_INDICATOR()
* colorDestroyedPart(mc, isDestroyed)
* colorWheelFromDmg(mc, dmg)
* SET_PART_TO_DESTROYED(part, isDestroyed)
* SET_WHEEL_DAMAGE(setWheel, setDmg)

 ORBITAL_CANNON_CAM
^^^^^^^^^^^^^^^^^^^

* ORBITAL_CANNON_CAM()
* INITIALISE(mc)
* SET_STATE(state)
* SET_MENU_TITLE(title)
* SET_MENU_HELP_TEXT(message)
* ADD_MENU_ITEM(id, leftText, rightText, isActive, strikethroughText)
* REMOVE_MENU_ITEM(id)
* SET_MENU_ITEM_STATE(id, isActive)
* SET_INPUT_EVENT(inputID)
* GET_CURRENT_SELECTION()
* SET_COUNTDOWN(value)
* SET_CHARGING_LEVEL(chargingLevel)
* SET_COOLDOWN_LEVEL(coolDownLevel)
* HIDE_COOLDOWN_METER()
* SHOW_COOLDOWN_METER()
* SET_ZOOM_LEVEL(zoomLevel)
* showMenu()
* showSurveillance()
* showManual()
* showAuto()
* clamp(value, min, max)
* setLocalisedText(tf, label)

 ORBITAL_CANNON_MAP
^^^^^^^^^^^^^^^^^^^

* ORBITAL_CANNON_MAP()
* initialise(mc)
* ZOOM_TO(normalisedZoom)
* MOVE_TO(px, py)
* CUT_TO_POSITION()
* START_CHARGING()
* START_COUNTDOWN()
* CANCEL_ANIMATION()
* update()

 ORGANISATION_NAME
^^^^^^^^^^^^^^^^^^

* ORGANISATION_NAME()
* INITIALISE(mc)
* SET_ORGANISATION_NAME(str, styleIndex, colourIndex, fontIndex)
* debug()

 OVERVIEW_BACKGROUND
^^^^^^^^^^^^^^^^^^^^

* OVERVIEW_BACKGROUND()
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 OVERVIEW_SCROLLER
^^^^^^^^^^^^^^^^^^

* OVERVIEW_SCROLLER()
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 PARTY_BUS
^^^^^^^^^^

* PARTY_BUS()
* INITIALISE(mc)
* initLightBar()
* initAnimations()
* initStrobe()
* initBeat()
* delegate(scope, method)
* update()
* onHideComplete(index)
* SET_MANUAL_OVERRIDE(isManual)
* SET_TEST_CARD(isShowing)
* BEAT()
* SHOW_ANIMATION(index, showImmediately)
* STROBE(normRate)

 PAUSE_MENU_AWARDS
^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_AWARDS()
* INITIALISE(mc)
* SET_DESCRIPTION()
* SET_INPUT_EVENT(direction)
* SET_HIGHLIGHT(i)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* ON_DESTROY()

 PAUSE_MENU_BODY_CONFIG_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_BODY_CONFIG_LIST()
* INITIALISE(mc)
* SET_INPUT_EVENT(direction)
* SET_HIGHLIGHT(i)

 PAUSE_MENU_CHARACTER_CARD
^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CHARACTER_CARD()
* INITIALISE(mc)
* SET_INPUT_EVENT(direction)
* SET_HIGHLIGHT(i)
* SET_FOCUS(isFocused)
* DISPLAY_VIEW(viewIndex, itemIndex)
* RESIZE_BG(i)
* SET_TITLE(titleStr, desc)
* SET_DESCRIPTION(helpStr, flashHelp)

 PAUSE_MENU_CHARACTER_SELECT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CHARACTER_SELECT()
* INITIALISE(mc)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_TITLE(str)
* SET_DESCRIPTION()
* SET_STATE(i)
* ON_DESTROY()
* SetCharacterProperties(index, visible, highlight)

 PAUSE_MENU_CREW_COMPARISON_CARD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CREW_COMPARISON_CARD()
* INITIALISE(mc)

 PAUSE_MENU_CREW_RANKS
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CREW_RANKS()
* INITIALISE(mc)
* SET_LINKED_LEADERBOARD(_crewsList)
* SHOW_COLUMN(bool)
* SET_FOCUS(isFocused)
* getKeys()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_CREWS_CARD
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CREWS_CARD()
* INITIALISE(mc, collapse)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_TITLE(titleStr)
* loadCardTexture(loaderMC, name, txd, txn, x, y, w, h)
* ON_DESTROY()
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_DESCRIPTION(descStr)
* getKeys()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_CREWS_LIST
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_CREWS_LIST()
* INITIALISE(mc)
* SET_HOVER_WIDTH(b)
* ADJUST_HOVER_WIDTH(b)
* SET_FOCUS(isFocused)
* SET_HIGHLIGHT(i)
* DISPLAY_VIEW(viewIndex, itemIndex)
* getKeys()
* SET_INPUT_EVENT(direction)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)

 PAUSE_MENU_DIALOGUE_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_DIALOGUE_LIST()
* INITIALISE(mc)
* rollOver()
* rollOut()
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)
* ON_DESTROY()

 PAUSE_MENU_FEED
^^^^^^^^^^^^^^^^

* PAUSE_MENU_FEED()
* INITIALISE(mc)
* rollOver()
* rollOut()
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_FOCUS(isFocused)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* ON_DESTROY()

 PAUSE_MENU_FREEMODE_MAP
^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_FREEMODE_MAP()
* INITIALISE(mc)
* SET_TITLE()

 PAUSE_MENU_FRIENDS_STATS_SP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_FRIENDS_STATS_SP()
* INITIALISE(mc)
* debug()
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)
* getKeys()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_GALLERY
^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_GALLERY()
* INITIALISE(mc)
* getKeys()
* SET_INPUT_EVENT(direction)
* getTxdData()
* SET_DESCRIPTION(max, date, location, track, visible)
* SET_TITLE(txd, txn, state)
* ADD_TXD_REF(txd, txn)
* CLEAR_SLOT()
* ON_DESTROY()
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_HIGHLIGHT(highlightIndex, staticClear)
* SET_COMPONENT_HIDDEN()
* SET_FOCUS(isFocused)

 PAUSE_MENU_HAIR_COLOUR_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_HAIR_COLOUR_LIST()
* INITIALISE(mc)
* SET_TITLE(str)
* btnScrollArrow(dir)
* btnPalette(index)
* SHOW_OPACITY(bool, opacityPosTop)
* SET_INPUT_EVENT(direction)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)
* itemSetData(i, cMC, cData)
* repositionPallattes()
* UPDATE_SLOT(_viewIndex, _slotIndex)
* SET_HIGHLIGHT(index)

 PAUSE_MENU_HERITAGE_CARD
^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_HERITAGE_CARD()
* INITIALISE(mc)
* SET_INPUT_EVENT(direction)
* SET_HIGHLIGHT(i)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* SET_TITLE(titleStr, desc)
* SET_DESCRIPTION(helpStr, flashHelp)
* getVisibleHeight()
* ON_DESTROY()

 PAUSE_MENU_MAP
^^^^^^^^^^^^^^^

* PAUSE_MENU_MAP()
* INITIALISE(mc)
* SET_TITLE(str)
* SET_DESCRIPTION()
* SET_HIGHLIGHT(i)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_INPUT_EVENT(input)
* SET_DATA_SLOT(sup)
* INIT_SCROLL_BAR(visible, columns, scrollType, arrowPosition, override, xColOffset)
* SET_SCROLL_BAR(currentPosition, maxPosition, maxVisible, caption)
* updateScroll()

 PAUSE_MENU_MISSION_HELP_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_MISSION_HELP_LIST()
* INITIALISE(mc)
* rollOver()
* rollOut()
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* SET_FOCUS(isFocused)
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_MISSION_REPLAY_CARD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_MISSION_REPLAY_CARD()
* INITIALISE(mc)
* SET_DATA_SLOT(_slotIndex)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* UPDATE_DATA_SLOT(_slotIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)
* clampText(textF, labelS, maxVal)
* SET_TITLE(title, desc)
* SET_DESCRIPTION(medalColourEnum, totalValue, totalLabel)
* SET_MEDAL(medalColourEnum)
* resizeBackground()

 PAUSE_MENU_NEWSWIRE
^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_NEWSWIRE()
* INITIALISE()
* rollOver()
* rollOut()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_PAGES_AWARDS
^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_AWARDS()
* setupPage()
* stateChanged(id)
* onPageExit()

 PAUSE_MENU_PAGES_CHAR_MOM_DAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CHAR_MOM_DAD()
* setupPage()
* setupColumns()
* stateChanged(id)

 PAUSE_MENU_PAGES_CHAR_SELECT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CHAR_SELECT()
* INITIALISE(mc)
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_CORONA
^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CORONA()
* setupPage()
* stateChanged(id)
* onPageExit()

 PAUSE_MENU_PAGES_CORONA_LOBBY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CORONA_LOBBY()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_CORONA_PLAYERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CORONA_PLAYERS()
* setupPage()
* stateChanged(id)
* onPageExit()

 PAUSE_MENU_PAGES_CORONA_RACE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CORONA_RACE()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_CREWS
^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_CREWS()
* setupPage()
* stateChanged(id)
* onPageExit()

 PAUSE_MENU_PAGES_FRIENDS
^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_FRIENDS()
* setupPage()
* stateChanged(id)
* onPageExit()

 PAUSE_MENU_PAGES_FRIENDS_MP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_FRIENDS_MP()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_GALLERY
^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_GALLERY()
* INITIALISE(mc)
* setupPage()
* stateChanged(id)
* onPageExit()

 PAUSE_MENU_PAGES_GAME
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_GAME()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_INFO
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_INFO()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_MAP
^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_MAP()
* setupPage()
* setDisplayConfig(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen)
* setScaledContent()
* stateChanged(id)

 PAUSE_MENU_PAGES_MISSIONCREATOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_MISSIONCREATOR()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_SAVE
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_SAVE()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_STATS
^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_STATS()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_STORE
^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_STORE()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_PAGES_WEAPONS
^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_PAGES_WEAPONS()
* setupPage()
* stateChanged(id)

 PAUSE_MENU_REPLAY_LIST
^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_REPLAY_LIST()
* INITIALISE(mc)
* SET_HIGHLIGHT(i)
* SET_INPUT_EVENT(direction)
* SET_DATA_SLOT_EMPTY(viewIndex, itemIndex)
* DISPLAY_VIEW(viewIndex, itemIndex)

 PAUSE_MENU_SPCHAR_OVERLAYS
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_SPCHAR_OVERLAYS()
* INITIALISE(mc)
* debug(id)
* LOAD_IMAGE(txd, xpos)
* createTexture(txD, txN, txX, txY, txW, txH)
* textureClear()
* textureLoaded()
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)

 PAUSE_MENU_STATS_LIST
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_STATS_LIST()
* INITIALISE(mc)
* rollOver()
* rollOut()
* SET_TITLE(str, highlightTitle)
* SET_DESCRIPTION(helpStr)
* DISPLAY_VIEW(viewIndex, itemIndex)
* SET_FOCUS(isFocused)
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_STATS_VERTICAL_LIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_STATS_VERTICAL_LIST()
* INITIALISE(mc)
* SET_HIGHLIGHT(i)
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_STORE_NEWS
^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_STORE_NEWS()
* INITIALISE(mc)

 PAUSE_MENU_TEXT_LIST_FULL
^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_TEXT_LIST_FULL()
* INITIALISE(mc)
* SET_FOCUS(isFocused)
* SET_HIGHLIGHT(i)
* getKeys()
* SET_INPUT_EVENT(direction)

 PAUSE_MENU_WEAPONS
^^^^^^^^^^^^^^^^^^^

* PAUSE_MENU_WEAPONS()
* INITIALISE(mc)
* SET_TITLE(str, id)
* SET_DESCRIPTION()
* SET_HIGHLIGHT(i)
* DISPLAY_VIEW(viewIndex, itemIndex)
* UPDATE_DATA_SLOT(_viewIndex, _slotIndex)

 PAUSE_MP_MENU_PLAYER_COMPARISON_CARD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* PAUSE_MP_MENU_PLAYER_COMPARISON_CARD()
* INITIALISE(mc)
* SET_TITLE(title)

 PLAYBACK_PANEL
^^^^^^^^^^^^^^^

* PLAYBACK_PANEL()
* SET_DISPLAY_CONFIG(screenWidthPixels, screenHeightPixels, safeTopPercent, safeBottomPercent, safeLeftPercent, safeRightPercent, isWideScreen, isHiDef, isAsian)
* initLayout()
* SET_PLAYBACK_BUTTONS_MODE(isFullyVisible)
* SET_TIMECODE(timecode)
* updateTimecodePosition()
* updateButtonsPosition()
* repositionButton(button)

 PLAYER_NAME
^^^^^^^^^^^^

* PLAYER_NAME()
* INITIALISE(mc)
* SET_PLAYER_NAME(str)
* SET_SPEAKER_STATE(state)
* debug()

 PLAYER_SWITCH
^^^^^^^^^^^^^^

* PLAYER_SWITCH()
* INITIALISE(mc, fileName)
* addDisplay()
* renderDisplay(index)
* SET_SWITCH_VISIBLE(bool)
* SET_SWITCH_SLOT(index, stateEnum, charEnum, selected, pedheadshot_txt_string)
* SET_MULTIPLAYER_HEAD(_newTXD)
* SET_SWITCH_HINTED(index, hinted)
* SET_SWITCH_HINTED_ALL(hinted0, hinted1, hinted2, hinted3)
* SET_PLAYER_DAMAGE(index, bVisible, bFlash)
* SET_SWITCH_COUNTER_ALL(count0, count1, count2, count3)
* setMissionText(mc, count)
* SET_PLAYER_SELECTED(sindex)
* SET_MP_LABEL(str)
* GET_SWITCH_SELECTED()
* ADD_TXD_REF_RESPONSE(txd, uniqueStr, success)
* loadComponent(txd, target, isDirectorMode)
* setupMasking()
* debug()

 PLAYER_SWITCH_STATS_PANEL
^^^^^^^^^^^^^^^^^^^^^^^^^^

* PLAYER_SWITCH_STATS_PANEL()
* INITIALISE(mc)
* SET_STATS_LABELS(charColourEnum)
* SHOW()
* HIDE()

 PLAYHEAD_MARKER
^^^^^^^^^^^^^^^^

* PLAYHEAD_MARKER()

 POWER_PLAY
^^^^^^^^^^^

* POWER_PLAY()
* INITIALISE(mc)
* initScreenLayout()
* SETUP_TEAM_COLOURS(teamOneColour, teamTwoColour)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept, _isAsian, _actualWidth, _actualHeight)
* SET_ICON_TIMERS(t1_ic1, t1_ic2, t1_ic3, t1_ic4, t1_ic5, t1_ic6, t2_ic1, t2_ic2, t2_ic3, t2_ic4, t2_ic5, t2_ic6)
* ACTIVATE_ICON(iconID, titleText, strapText, greyOtherIcons, teamColourID)
* REMOVE_SRPRESSED_STATE()
* animateIcon(iconID, style)
* surpressIcons()
* loop()
* OVERRIDE_DURATION(dur)
* SET_MESSAGE_VISIBILITY(isVisible)
* log(str)

 POWER_PLAY_BIKER
^^^^^^^^^^^^^^^^^

* POWER_PLAY_BIKER()
* INITIALISE(mc)
* SETUP_TEAM_COLOURS(teamOneColour, teamTwoColour, teamThreeColour, teamFourColour)
* SET_ICON_TIMERS(t1_ic1, t1_ic2, t1_ic3, t2_ic1, t2_ic2, t2_ic3, t3_ic1, t3_ic2, t3_ic3, t4_ic1, t4_ic2, t4_ic3)
* REMOVE_SRPRESSED_STATE()
* surpressIcons()
* animateIcon(iconID, style)
* loop()
* OVERRIDE_DURATION(dur)
* SET_MESSAGE_VISIBILITY(isVisible)
* log(str)

 POWER_PLAY_DAY_NIGHT
^^^^^^^^^^^^^^^^^^^^^

* POWER_PLAY_DAY_NIGHT()
* INITIALISE(mc)
* SET_INITIAL_ICON(iconType)
* SETUP_TEAM_COLOURS(teamOneColour, teamTwoColour)
* SET_ICON_TIMERS(t1_ic1, t1_ic2, t2_ic1, t2_ic2)
* REMOVE_SRPRESSED_STATE()
* surpressIcons()
* animateIcon(iconID, style)
* ACTIVATE_ICON(iconID, titleText, strapText, greyOtherIcons, teamColourID)
* loop()

 POWER_PLAY_GENERIC
^^^^^^^^^^^^^^^^^^^

* POWER_PLAY_GENERIC()
* INITIALISE(mc)
* ADD_TEAM(hudColourEnum)
* ADD_ICON(type)
* PULSE_ICON(iconIndex, teamIndex)
* SET_ICON_SCORE(iconIndex, score, teamIndex)
* SET_ICON_TIMER(iconIndex)
* SET_ICON_METER(iconIndex)
* ACTIVATE_ICON(iconIndex, teamIndex)
* DEACTIVATE_ICON(iconIndex)
* DEACTIVATE_ALL_ICONS()
* SHOW_MESSAGE(title, strapline, teamIndex)
* HIDE_MESSAGE()
* updateLayout()
* layoutIconRow(iconDiameter, y, startIndex, endIndex)

 POWER_PLAY_SPECIAL_RACES
^^^^^^^^^^^^^^^^^^^^^^^^^

* POWER_PLAY_SPECIAL_RACES()
* INITIALISE(mc)
* REMOVE_ICON(index)
* SETUP_TEAM_COLOURS(teamOneColour, teamTwoColour, teamThreeColour, teamFourColour)
* SET_ICON_TIMERS()
* SET_ICON_TIMER(iconIndex, team1Value, team2Value, team3Value, team4Value)
* SET_ICON_BACKGROUND(iconID, teamColourID)
* RESET_ICON_BACKGROUNDS()
* REMOVE_SRPRESSED_STATE()
* surpressIcons()
* animateIcon(iconID, style)
* loop()
* OVERRIDE_DURATION(dur)
* SET_MESSAGE_VISIBILITY(isVisible)
* initIcons(teamOneColourHex, teamTwoColourHex, teamThreeColourHex, teamFourColourHex)

 POWER_PLAY_TURF
^^^^^^^^^^^^^^^^

* POWER_PLAY_TURF()
* INITIALISE(mc)
* SET_NUMBER_OF_TEAMS(numTeams)
* SETUP_TEAM_COLOURS(teamOneColour, teamTwoColour, teamThreeColour, teamFourColour)
* SET_TEAM_SCORES(t1, t2, t3, t4)
* SET_ICON_TIMERS(t1_ic1, t2_ic1, t3_ic1, t4_ic1, t5_ic1, timerTeamColour)
* REMOVE_SRPRESSED_STATE()
* PULSE_ICON(iconID, pulseCount)
* addIconsToStage()
* surpressIcons()
* animateIcon(iconID, style)
* loop()
* OVERRIDE_DURATION(dur)
* SET_MESSAGE_VISIBILITY(isVisible)
* log(str)

 POWER_PLAY_VEHICLE
^^^^^^^^^^^^^^^^^^^

* POWER_PLAY_VEHICLE()
* INITIALISE(mc)
* REMOVE_ICON(index)
* SETUP_TEAM_COLOURS(teamOneColour, teamTwoColour)
* initIcons(teamOneColourHex, teamTwoColourHex)
* ACTIVATE_ICON(iconID, titleText, strapText, greyOtherIcons, teamColourID)
* SET_ICON_BACKGROUND(iconID, teamColourID)
* RESET_ICON_BACKGROUNDS()
* SET_ICON_TIMERS(t1_ic1, t1_ic2, t1_ic3, t1_ic4, t1_ic5, t1_ic6, t1_ic7, t1_ic8, t1_ic9, t1_ic10, t2_ic1, t2_ic2, t2_ic3, t2_ic4, t2_ic5, t2_ic6, t2_ic7, t2_ic8, t2_ic9, t2_ic10)
* REMOVE_SRPRESSED_STATE()
* surpressIcons()
* animateIcon(iconID, style)

 PSYCHOLOGY_REPORT
^^^^^^^^^^^^^^^^^^

* PSYCHOLOGY_REPORT()
* INITIALISE(mc)
* SET_PLAYER_NAME(gamerTitle, gamerTag, crewtag)

 RACE_MESSAGE
^^^^^^^^^^^^^

* RACE_MESSAGE()
* INITIALISE(mc)
* debug()
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept, _isAsian, _actualWidth, _actualHeight)
* SET_RACE_MESSAGE(titleText, strapText, iconID)
* REMOVE_MESSAGE()
* OVERRIDE_DURATION(dur)
* SET_MESSAGE_VISIBILITY(isVisible)
* log(str)

 RACE_POSITION
^^^^^^^^^^^^^^

* RACE_POSITION()
* INITIALISE(mc)
* getKeys()
* debug()
* setText(tf, txt, alignLeft)
* setResults()
* createResults()
* SET_RACE_LABELS(racePosLabel, raceTimeLabel, bestTimeLabel, gateCounterLabel, raceResultsLabel)
* SHOW_RACE_MODULE(enum, show)
* SET_RACE_POSITION(_position, _racers)
* SET_GATES_POSITION(_gateposition, _gates)
* SET_RACE_TIME(_time)
* SET_BEST_TIME(_time)
* SET_RACE_RESULTS(_index, _position, _racer, _time)
* SHOW_RACE_RESULTS(vis)

 RAMPAGE
^^^^^^^^

* RAMPAGE()
* INITIALISE(mc)
* SHOW_RAMPAGE()
* HIDE_RAMPAGE()
* SHOW_RAMPAGE_INTRO(duration, rampage, description)
* SHOW_RAMPAGE_COUNTDOWN(duration, description)
* SHOW_RAMPAGE_OUTRO()
* setAlpha(_mc)
* swapAlpha(_mc1, _mc2)
* bounceBack(duration, _mc)

 REMOTE_SNIPER_HUD
^^^^^^^^^^^^^^^^^^

* REMOTE_SNIPER_HUD()
* INITIALISE(mc)
* loadingAnimation()
* debug()
* update()
* initScreenLayout()
* SET_ZOOM_LEVEL(zoomLevel)
* SET_WIND(windValue, directionIsRight)
* SET_COMPASS(a)
* setCompassPointPos(mc, a, index)

 REMOTE_SNIPER_LOADING
^^^^^^^^^^^^^^^^^^^^^^

* REMOTE_SNIPER_LOADING()
* INITIALISE(mc)
* START_LOADING()

 ROUND_DECIMAL_PLACES
^^^^^^^^^^^^^^^^^^^^^

* ROUND_DECIMAL_PLACES()

 SAVING_FOOTER
^^^^^^^^^^^^^^

* SAVING_FOOTER()
* INITIALISE(mc)
* SET_TEXT()
* SET_WAITING_TEXT()
* setSaveText(str)
* setDropShadow()

 SCORE_CLIP
^^^^^^^^^^^


 SECURITY_CAM
^^^^^^^^^^^^^

* SECURITY_CAM()
* INITIALISE(mc)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* initScreenLayout()
* SET_LAYOUT(type)
* SET_LOCATION(loc)
* SET_DETAILS(details)
* SET_TIME(hh, mm, ss, tt)

 SECURITY_CAMERA
^^^^^^^^^^^^^^^^

* SECURITY_CAMERA()
* INITIALISE(mc)
* SHOW_CAMERA_OVERLAY()
* SHOW_STATIC()

 SECUROSERV
^^^^^^^^^^^

* SECUROSERV()
* initialise(mc)
* ACTIVATE()
* DEACTIVATE()
* SET_PLAYER_DATA(gamerTag, gamerHasAccess, totalEarnings, collectionsCompleted, collectionSuccessRate, salesCompleted, salesSuccessRate, organisation, numVehiclesStolen, stealVehiclesSuccess, vehiclesExported, exportVehiclesSuccess, totalVehicleEarnings, hasSpecialVehicleMissions, playerX, playerY)
* ADD_ACTIVE_USER(gamerTag, organisation, goon1, goon2, goon3, goon4, goon5, goon6, goon7)
* REMOVE_ACTIVE_USER(gamerTag)
* ADD_WAREHOUSE(id, x, y, purchaseCost, nameLabel, locationLabel, descriptionLabel, txd, isOwned, size, capacity, amountStored, currentValue, sellCooldown, buyCooldown, displayOrder, purchaseSaleCost)
* ADD_WAREHOUSE_SHIPMENTS(id, smallShipmentSize, smallShipmentCost, shipmentDescription, mediumShipmentSize, mediumShipmentCost, mediumShipmentDescription, largeShipmentSize, largeShipmentCost, smallShipmentIsSpecial, smallShipmentSaleCost, mediumShipmentSaleCost, largeShipmentSaleCost)
* ADD_VEHICLE_WAREHOUSE(id, x, y, interior0Cost, interior0SaleCost, interior1Cost, interior1SaleCost, interior2Cost, interior2SaleCost, warehouseName, location, description, txd, isOwned, vehicleCapacity, numVehiclesStored, currentValue, stealCooldown, purchasedInterior)
* ADD_SPECIAL_VEHICLE(id, name, description, txd, lockNum, enabled, cashBonus, rpBonus)
* UPDATE_COOLDOWN(remainingSeconds)
* SHOW_OVERLAY(titleLabel, messageLabel, acceptButtonLabel, cancelButtonLabel, success, showInteriorsOverlay)
* HIDE_OVERLAY()
* GET_SELECTED_WAREHOUSE_ID()
* GET_CURRENT_SELECTION()
* GET_CURRENT_SCREEN_ID()
* IS_WAREHOUSE_PANEL_SHOWING()
* SET_INPUT_EVENT(inputID)
* SET_INPUT_RELEASE_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* showScreen(screenID)
* getWarehouseByID(id)
* getVehicleWarehouseByID(id)
* quit()
* TXD_HAS_LOADED(txd, success, id)

 SETTINGS
^^^^^^^^^

* SETTINGS()
* construct()
* populateContent()
* setIcon(target, menuIconFrameEnum)
* setState(item, isActive)

 SHOP_MENU
^^^^^^^^^^

* SHOP_MENU()
* INITIALISE(mc)
* SET_DATA_SLOT(_slotIndex)
* UPDATE_DATA_SLOT(_slotIndex)
* DRAW_MENU_LIST(visItems)
* SET_LOGO(brandID)
* SET_HEADER(newHeader)
* SET_POPUP(dialogStr, delay)
* FADE_POPUP_OUT()
* RESIZE_BACKGROUND(_viewIndex)
* SHOW_SCROLL_HINTS(show)
* SET_INPUT_EVENT(direction)

 SHOP_MENU_DLC
^^^^^^^^^^^^^^

* SHOP_MENU_DLC()
* INITIALISE(mc)
* GET_CURRENT_SELECTION()
* SET_DATA_SLOT_EMPTY(clearEverything)
* SET_DATA_SLOT(_slotIndex)
* UPDATE_DATA_SLOT(_slotIndex)
* DRAW_MENU_LIST()
* DISPLAY_DATA_SLOT()
* SET_TITLE(newHeader)
* SET_IMAGE(textureDict, textureFilename)
* SET_DESCRIPTION(description, priceTitle, priceValue)
* RESIZE_BACKGROUND(_viewIndex)
* SHOW_SCROLL_HINTS()
* SET_INPUT_EVENT(direction)

 SHUTTER
^^^^^^^^

* SHUTTER()
* construct()
* populateContent()
* CLEAN_UP_DATA()
* CLOSE_APP()

 SLOT_MACHINE
^^^^^^^^^^^^^

* SLOT_MACHINE()
* initialise(mc)
* initText()
* SET_MESSAGE(Message)
* SET_BET(Bet)
* SET_LAST_WIN(LastWin)
* SET_THEME(Theme)
* colorSlotText(colorValue)
* colorSlotNumbers(colorValue)
* resizeAsianText(tf)

 SOCIAL_CLUB_TV
^^^^^^^^^^^^^^^

* SOCIAL_CLUB_TV()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SHOW_LIVE_PANEL(value)
* SET_LIVE_PANEL(title, description, player, crewTag, txd, txn)
* SHOW_TICKER(value)
* SET_TICKER_TITLE(title)
* ADD_TICKER_TEXT()
* ADD_TXD_REF_RESPONSE(txd, strRef, success)
* _positionLivePanel()
* _positionLowerThird()
* _howWide(target)

 SP_PLAYER_CARD
^^^^^^^^^^^^^^^

* SP_PLAYER_CARD()
* INITIALISE(mc)
* getMovieID()
* SET_TITLE(titleStr, crewTagStr, hudColourEnum)
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* updateStatWheel(index, pctComplete, statColourEnum)
* drawArc(startAngle, endAngle, colourId)
* lineToPtOnWheel(angle)
* SET_DATA_SLOT_EMPTY()

 SP_PLAYER_COMPARISON_CARD
^^^^^^^^^^^^^^^^^^^^^^^^^^

* SP_PLAYER_COMPARISON_CARD()
* getMovieID()

 SPEED_INDICATOR
^^^^^^^^^^^^^^^^

* SPEED_INDICATOR()
* INIT_SPEED_INDICATOR(stateId, width)
* DISPOSE()

 SPLASH_TEXT
^^^^^^^^^^^^

* SPLASH_TEXT()
* INITIALISE(mc)
* SET_SPLASH_TEXT(txt, duration, r, g, b, a)
* SPLASH_TEXT_LABEL(txt, r, g, b, a)
* SPLASH_TEXT_COLOR(r, g, b, a)
* SPLASH_TEXT_TRANSITION_IN(duration, managed)
* _handleTransitionInComplete()
* SPLASH_TEXT_TRANSITION_OUT(duration, managed)
* _handleTransitionOutComplete()
* IS_SPLASH_TEXT_VISIBLE()

 SPPED_INDICATOR
^^^^^^^^^^^^^^^^


 STAGE
^^^^^^

* STAGE()
* SET_STAGE_TEXT(str)
* clearBlipLayer()
* onPress()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 STAGE_CLIP
^^^^^^^^^^^


 STARTER_PACK_BROWSER
^^^^^^^^^^^^^^^^^^^^^

* STARTER_PACK_BROWSER()
* initialise(mc)
* showScreen(screenID)
* setActiveItem(activeItem)
* setActiveCategory(activeCategory)
* TXD_HAS_LOADED(txd, success, id)
* SET_INPUT_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_MOUSE_INPUT(x, y)
* PURCHASE_BUTTONS_VISIBLE(isVisible)
* GET_CURRENT_ITEM()
* GET_CURRENT_SCREEN()
* ADD_ITEM(id, category, title, description, textureDictionary, texture, link, equipped, subCategory, thumbTextureDictionary, thumbTexture)
* REMOVE_ITEM(id)
* setLocalisedText(tf, label)
* truncate(tf, txt, autoSize, letterSpacing)
* setEllipsis(label, tf)
* formatNumber(value)
* delegate(scope, method)
* playSound(soundName)

 STORE_BACKGROUND
^^^^^^^^^^^^^^^^^

* STORE_BACKGROUND()
* INITIALISE(mc)
* fadeInBackground()
* ANIMATE_BACKGROUND(_speed)
* scrollUp(mc, _speed)
* scrollDown(mc, _speed)

 STORE_BLACKOUT
^^^^^^^^^^^^^^^

* STORE_BLACKOUT()
* INITIALISE(mc)
* FADE_TO_BLACK(_speed)
* CALL_FADETOBLACK_COMPLETED()
* FADE_TO_TRANSPARENT(_speed)
* CALL_FADETOTRANSPARENT_COMPLETED()

 STORE_CONTENTIMAGE_LIST
^^^^^^^^^^^^^^^^^^^^^^^^

* STORE_CONTENTIMAGE_LIST()
* SETUP_COLUMN(mc, _menuBgCol, _blackCol, _whiteCol)
* SET_DATA(_slot, _data)
* SET_DATA_EMPTY(_slot)
* setImageHeight()
* UPDATE_CONTENTIMAGE_SIZE(_maxVisItems)
* removeAllSlots()
* highlightItem(_slot)
* REDRAW()
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* updateScrollIndicator()
* SET_INPUT_EVENT(direction)
* GET_CURRENT_SELECTION()
* highlight(_slot, _h)
* SET_FOCUS(isFocused)
* CURRENT_COLUMN(_column)

 STORE_DETAILS_LIST
^^^^^^^^^^^^^^^^^^^

* STORE_DETAILS_LIST()
* SETUP_COLUMN(mc, _menuBgCol, _blackCol, _whiteCol)
* SET_DATA(_slot, _data)
* SET_DATA_EMPTY(_slot)
* highlightItem(_slot)
* SET_DESCRIPTION(priceTitle, itemPrice, numPlayers, statusText, statusColour, priceVis, playersVis, statusVis)
* REDRAW()
* COLOUR_STATUS_BAR()
* UPDATE_STATUS_COLOURS(_bgCol, _textCol)
* SET_INPUT_EVENT(direction)
* GET_CURRENT_SELECTION()
* updateScrollIndicator()
* highlight(_h)
* SET_FOCUS(isFocused)
* CURRENT_COLUMN(_column)
* parseLinebreaks(str)

 STORE_VERTICAL_LIST
^^^^^^^^^^^^^^^^^^^^

* STORE_VERTICAL_LIST()
* SETUP_COLUMN(mc, _menuBgCol, _blackCol, _whiteCol)
* REDRAW()
* SET_DATA(_slot, _data)
* SET_DATA_EMPTY(_slot)
* highlightItem(_slot)
* updateScrollIndicator()
* SET_INPUT_EVENT(direction)
* GET_CURRENT_SELECTION()
* highlight(_slot, _h)
* SET_FOCUS(isFocused)
* CURRENT_COLUMN(_column)

 STRENGTH_TEST_SCORE
^^^^^^^^^^^^^^^^^^^^

* STRENGTH_TEST_SCORE()
* initialise(mc)
* SET_SCORE(value, countUpDuration, holdDuration, countDownDuration)
* SET_INSTANT_SCORE(value)
* SET_HIGH_SCORE(value, countUpDuration, holdDuration, countDownDuration)
* SET_INSTANT_HIGH_SCORE(value)

 STUNT_JUMPS
^^^^^^^^^^^^

* STUNT_JUMPS()
* INITIALISE(mc)
* SET_STUNT_JUMP_TITLE_AND_DESCRIPTION(stuntJumpTitle, stuntJumpDescription, stuntJumpProgress)
* SET_STUNT_JUMP_COLOR(hudColourId)
* SET_VISIBLE(isVisible)
* debug()
* OVERRIDE_Y_POSITION(newYPosition)
* SHOW_SHARD_STUNT_JUMP(bigText, msgText)
* SHARD_SET_TEXT(bigText, msgText)
* SHARD_ANIM_OUT(colID, animTime)

 SUB_CAM
^^^^^^^^

* SUB_CAM()
* INITIALISE(mc)
* debug()
* update()
* initScreenLayout()
* SET_COMPASS_POINT_POS(mc, a, index)
* SET_CAM_HEADING(a)
* SET_CAM_FOV(a)
* SET_CAM_ALT(a)
* SET_CAM_CURSOR_POS(x, y)

 SUB_PC
^^^^^^^

* SUB_PC()
* INITIALISE(mc)
* debug()
* getKeys()
* initScreenLayout()
* SET_INPUT_EVENT(direction)
* SET_INPUT_EVENT_SELECT()
* ADD_PROGRAM(i, enum, lbl)
* RUN_PROGRAM(id)
* OPEN_POPUP(i)
* SET_DATA_SLOT(i, id, x, y, t)
* SET_PC_NEEDED(i)
* IS_PC_NEEDED()
* ADD_BUTTONS(m)
* ACTIVATE_BUTTONS(m, b)
* REMOVE_BUTTONS(m)
* SET_SNAP_SPEED(s)
* MOVE_CURSOR(vx, vy)
* CheckUnderCursor()
* snapToButton()
* snapToButtonComplete()
* testList(list)
* RESET_UNDER_CURSOR()
* CURSOR_CLICK()
* LAST_POPUP_CLOSED()
* openApp(i)
* closeApp(id)
* SET_LABELS(sluiceLbl, techLbl, securityLbl, accessLbl)
* SET_DATE(days, months, years)
* SET_TIME(hours, mins)
* SET_SECTION(section, cam, action1Lbl, action2Lbl)
* TRIGGER_CAM_FLASH()
* TRIGGER_WARNING(num)
* SET_BUTTON_ACTIVE(buttonEnum, isActive)

 TATTOO_BUTTONS
^^^^^^^^^^^^^^^

* TATTOO_BUTTONS()
* INITIALISE(mc)
* debug()
* getKeys()
* ADD_BUTTON(whichButton)
* FADE_OUT_OLD_BUTTON()
* REORDER_BUTTONS_ARRAY()
* SET_STICK_POINTER_ANGLE(arAngle, color)
* HIDE_STICK_POINTER()

 TAXI_DISPLAY
^^^^^^^^^^^^^

* TAXI_DISPLAY()
* INITIALISE(mc)
* ADD_TAXI_DESTINATION(positionInList, blip, r, g, b, destination, addressOne, addressTwo, isAsian)
* SHOW_TAXI_DESTINATION()
* HIGHLIGHT_DESTINATION(forceDestination)
* SET_TAXI_PRICE(newPrice, isAsian)
* CLEAR_TAXI_DISPLAY()
* SET_DATA_SLOT(_slotIndex)
* UPDATE_DATA_SLOT(_slotIndex)
* SET_DATA_SLOT_EMPTY()

 TEETH_PULLING
^^^^^^^^^^^^^^

* TEETH_PULLING()
* INITIALISE(mc)
* update()
* tortureSuccess()
* tortureFail()
* SET_TEETH_BRITTLE(amount)
* SET_TEETH_ANGLE(amount)
* SET_TEETH_DEPTH(amount)
* CLEANUP_MOVIE()

 TEXT_CANVAS
^^^^^^^^^^^^

* TEXT_CANVAS()
* INITIALISE(mc)
* SET_ASPECT_RATIO(xRatio, yRatio)
* BEGIN_SETUP_TEMPLATE(templateTypeId)
* UPDATE_PROPERTY()
* END_SETUP_TEMPLATE()
* START_TEMPLATE()
* PAUSE_TEMPLATE()
* DISPOSE()
* initCustomTemplate(templateTypeId)

 TEXT_CLIP
^^^^^^^^^^

* TEXT_CLIP()
* SET_TEXT_WITH_WIDTH(str, bgWidth, showFadeOut)
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 TEXT_INPUT_BOX
^^^^^^^^^^^^^^^

* TEXT_INPUT_BOX()
* INITIALISE(mc)
* SET_TEXT_BOX()
* SET_MULTI_LINE()
* UPDATE_DISPLAY_PARAMS()
* UPDATE_INPUT(text, cursorLocation)
* SET_CURSOR_LOCATION(cursorLocation)
* CLEANUP()
* HANDLE_KEY_PRESS(key)
* clearCursorHistory()
* onMouseDown()
* onMouseUp()
* onMouseMove()
* dispatchCursorLocationChange(bForceDispatch)

 TEXT_MESSAGE_LIST
^^^^^^^^^^^^^^^^^^


 TEXT_MESSAGE_VIEW
^^^^^^^^^^^^^^^^^^


 TEXTFIELD
^^^^^^^^^^

* TEXTFIELD()
* INITIALISE(mc)
* SET_BACKGROUND_IMAGE(txd, txn, alpha)
* SET_TEXT_POINT_SIZE(size)
* SET_TEXT(str)
* CLEAR_BACKGROUND_IMAGE()
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* startNewTextureLoad(txd, txn)
* resizeBackground()

 THUMBNAIL_CLIP
^^^^^^^^^^^^^^^


 TIMECODE_MC
^^^^^^^^^^^^

* TIMECODE_MC()
* SET_TIMECODE(str)
* SET_RADIO_TRIMMING_LINE_VISIBILITY(isLineVisible, isIconVisible)

 TIMECODE_NEW
^^^^^^^^^^^^^


 TIMELINE_PANEL
^^^^^^^^^^^^^^^


 TRAFFIC_CAM
^^^^^^^^^^^^

* TRAFFIC_CAM()
* INITIALISE(mc)
* debug()
* update()
* initScreenLayout()
* PLAY_CAM_MOVIE()
* SET_LAT_LONG(lat1, lat2, lon1, lon2)
* SET_CAM_DATE(day, hrs, min)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept)

 TURRET_CAM
^^^^^^^^^^^

* TURRET_CAM()
* INITIALISE(mc)
* initScreenLayout()
* SET_COMPASS_POINT_POS(mc, a, index)
* SET_CAM_HEADING(a)
* SET_CAM_FOV(a)
* SET_CAM_ALT(a)
* SET_ALT_FOV_HEADING(a, f, h)
* SET_CAM_LOGO(value)

 TV_FRAME
^^^^^^^^^

* TV_FRAME()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)

 VAULT_DRILL
^^^^^^^^^^^^

* VAULT_DRILL()
* INITIALISE(mc)
* SET_POSITION(normX, normY)
* SET_NUM_DISCS(numDiscs)
* REVEAL()
* SET_SPEED(speed)
* SET_HOLE_DEPTH(depth)
* SET_DRILL_POSITION(position)
* SET_TEMPERATURE(temperature)
* RESET()
* update()
* updateDrillRotation()
* updateOverheat()
* updateDiscs(y, allowHoleFilling)
* shake()
* fadeInSparks()
* fadeOutSparks()
* burstOutSparks()
* fadeOutSparksComplete()
* setDiscHighlight(discIndex)
* flashDiscHighlight()
* showNumber(value, view)

 VAULT_LASER
^^^^^^^^^^^^

* VAULT_LASER()
* INITIALISE(mc)
* SET_POSITION(normX, normY)
* SET_NUM_DISCS(numDiscs)
* REVEAL()
* SET_HOLE_DEPTH(depth)
* SET_DRILL_POSITION(position)
* SET_TEMPERATURE(temperature)
* SET_LASER_WIDTH(width)
* SET_LASER_VISIBLE(isVisible)
* RESET()
* update()
* updateOverheat()
* updateDiscs(y, allowHoleFilling)
* shake()
* fadeInSparks()
* fadeOutSparks()
* burstOutSparks()
* fadeOutSparksComplete()
* setDiscHighlight(discIndex)
* flashDiscHighlight()
* showNumber(value, view)

 VIDEO_BUTTON_TYPES
^^^^^^^^^^^^^^^^^^^

* VIDEO_BUTTON_TYPES()

 VIDEO_CLIP
^^^^^^^^^^^

* VIDEO_CLIP()
* onPress()
* onRollOver()
* onRollOut()
* onRelease()
* onReleaseOutside()
* sendMouseEvent(evt)

 WAREHOUSE
^^^^^^^^^^

* WAREHOUSE()
* initialise(mc)
* SET_WAREHOUSE_DATA(nameLabel, locationLabel, txd, size, capacity, amountStored, currentValue, specialItems, sellCooldown)
* SET_PLAYER_DATA(gamerTag, organizationName, sellerRating, numSales, totalEarnings)
* SET_BUYER_DATA(buyerOrganization0, amount0, offerPrice0, buyerOrganization1, amount1, offerPrice1, buyerOrganization2, amount2, offerPrice2, buyerOrganization3, amount3, offerPrice3)
* ADD_ACTIVE_USER(gamerTag, organisation)
* REMOVE_ACTIVE_USER(gamerTag)
* SHOW_OVERLAY(titleLabel, messageLabel, acceptButtonLabel, cancelButtonLabel, success)
* HIDE_OVERLAY()
* GET_CURRENT_SELECTION()
* SET_INPUT_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* TXD_HAS_LOADED(txd, success, id)

 WATERMARK
^^^^^^^^^^

* WATERMARK()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, isWideScreen, _isHiDef, _isAsian)
* INITIALISE(mc)
* SET_WATERMARK_TYPE(type, screenWidthPixels, screenHeightPixels)
* Is16to10(screenWidthPixels, screenHeightPixels)
* SET_WATERMARK_LABELS(userLabel, movieNameLabel)
* START_ANIMATION()
* RESUME_ANIMATION()
* PAUSE_ANIMATION()
* dispose()
* update()
* resetMasksAndCounter()
* calculatePercentageDifference(valueA, valueB)

 WIND_METER
^^^^^^^^^^^

* WIND_METER()
* INITIALISE(_mc)
* SET_WIND_DIRECTION(rotation, strg)
* SET_COMPASS_DIRECTION(rotation)
* TINT_WIND_POINTER(id, r, g, b)
* initCompass()
* setCompass(a)
* setCompassPoint(mc, a, index)

 XYZ
^^^^

* XYZ()
* construct()
* renderContainers()
* populateContent()
* CLOSE_APP()

 YACHT_NAME
^^^^^^^^^^^

* YACHT_NAME()
* INITIALISE(mc)
* SET_YACHT_NAME(str, isWhiteText, country)
* debug()

 YACHT_NAME_STERN
^^^^^^^^^^^^^^^^^

* YACHT_NAME_STERN()
* INITIALISE(mc)
* SET_YACHT_NAME(str, isWhiteText, country)
* debug()

 YOGA_BUTTONS
^^^^^^^^^^^^^

* YOGA_BUTTONS()
* INITIALISE(mc)
* ADD_BUTTON_TO_LIST(buttonID)
* DRAW_BUTTONS()
* REMOVE_BUTTONS(buttonID)
* SET_BUTTON_TARGET(buttonID, targetScale, whichTarget, r, g, b, a)
* SET_HOLD_TIMER(timePercent)
* SET_PLAYER_INPUT_COLOUR(buttonID, r, g, b, a)
* SET_OUT_RING_TIMER_COLOUR(buttonID, r, g, b, a)
* SET_OUT_RING_TIMER(buttonID, percent)
* SET_INFO_TIMER(timePercent)
* SET_STICK_POINTER_ANGLE(buttonID, arAngle)
* SET_STICK_POINTER_RGB(buttonID, r, g, b)
* SET_STICK_ANGLE(buttonID, arAngle)
* BUTTON_PRESSED(buttonID, buttonPercent)
* BUTTON_DEPRESSED(buttonID)
* BUTTON_STATE(buttonID, buttonState)
* ButtonReset(button)
* TOGGLE_INPUT_FILL(shouldUseFill)
* SET_STICK_POINTER_HIGHLIGHT_ANGLE(buttonID, arAngle)
* HIDE_STICK_POINTER(buttonID)

 generic_2
==========

 DIGITAL_SAFE_DISPLAY
^^^^^^^^^^^^^^^^^^^^^

* DIGITAL_SAFE_DISPLAY()
* initialise(mc)
* SET_STATE(state)
* SET_CURSOR_POSITION(position)
* SET_VALUE(position, value)
* CLEAR_VALUE(position)
* show(display, colour)
* hideCursor()
* restoreView()
* clamp(value, min, max)
* setChar(display, char)

 ISLAND_HEIST_BOARD
^^^^^^^^^^^^^^^^^^^

* ISLAND_HEIST_BOARD()
* initialise(mc)
* SHOW_SCREEN(screenID)
* SHOW_OVERLAY(title, message, acceptButtonLabel, cancelButtonLabel)
* HIDE_OVERLAY()
* REQUEST_CURRENT_SELECTION()
* REQUEST_CURRENT_ROLLOVER()
* SET_INPUT_EVENT(inputID)
* SET_CURRENT_SELECTION(itemID)
* SET_TABS(tab1Label, tab1Locked, tab2Label, tab2Locked, tab3Label, tab3Locked)
* ADD_SETUP_ITEM(tabID, parentID, itemID, title, numComplete, numTotal, locked, isMandatory, description, texture, showDollar, count, countMax)
* ADD_FINALE_ITEM(parentID, itemID, title, isSelected, description, texture, locked, showDollar)
* SET_FINALE_MENU_IDS(timeOfDayID, approachVehicleID, entryPointID, exitPointID, weaponsID, supportCrewID, crewCutID, compoundEntryPointID)
* SET_INITIAL_TAB_VIEW(initialView)
* SET_IS_HARD_MODE(isHardMode)
* SET_PAYOUTS(isVisible, mainPayout, subPayout, mainPayoutLabel, subPayoutLabel)
* SET_FINALE_COST(itemID, cost)
* ADD_MAP_ICON(setupItemID, finaleItemID, iconID, mapID, x, y)
* ADD_WORLD_MAP_ICON(setupItemID, finaleItemID, iconID, mapID, x, y)
* SHOW_TIP_TEXT(text)
* HIDE_TIP_TEXT()
* SET_FINALE_ITEM_SELECTED(itemID, isSelected)
* SET_SETUP_ITEM_NUM_COMPLETE(itemID, numComplete)
* REMOVE_FINALE_ITEM(itemID)
* SET_CREW_MEMBER(id, gamertag, percentage, headsetState, isReady)
* CLEAR_CREW_MEMBER(id)
* SET_LAUNCH_BUTTON(isEnabled, label)
* SET_CREW_CUTS_VISIBLE(isVisible)
* SET_MAP_VIEW(mapView)
* SET_FINALE_LIST_TITLE(title)
* showScreen(screenID)
* updateButtons(activeButtonIndex)
* TXD_HAS_LOADED(txd, success, id)

 SUBMARINE_MISSILES
^^^^^^^^^^^^^^^^^^^

* SUBMARINE_MISSILES()
* INITIALISE(mc)
* SET_ZOOM_VISIBLE(isVisible)
* SET_WARNING_IS_VISIBLE(isVisible)
* SET_WARNING_FLASH_RATE(normRate)
* startFlash()
* stopFlash()
* updateFlash()
* setLocalisedText(tf, label, letterSpacing)

 heist_mp
=========

 HACKING_MESSAGE
^^^^^^^^^^^^^^^^

* HACKING_MESSAGE()
* INITIALISE(mc)
* SET_DISPLAY(unlockId, title, message, red, green, blue, stagePassed)
* executeLockAnim(unlockId)
* playLesterLaughSound()
* playUnlockSound()
* initLesterBounce()

 HEIST_CELEBRATION
^^^^^^^^^^^^^^^^^^

* HEIST_CELEBRATION()
* INITIALISE(mc, type)
* registerSyncedMovie(id, sequenceTypeBit)
* syncPointClear(id)
* PAUSE()
* SET_PAUSE_DURATION()
* CREATE_STAT_WALL(id, bgColourId, sfxId)
* ADD_BACKGROUND_TO_WALL(id, alpha, moneyMesh)
* ADD_MISSION_RESULT_TO_WALL(id, missionTextLabel, passFailTextLabel, messageLabel, isMessageRawText, isPassFailRawText, isMissionTextRawText)
* ADD_COMPLETE_MESSAGE_TO_WALL(id, missionTextLabel, completeTextLabel, messageLabel, isMessageRawText, isCompleteRawText, isMissionTextRawText)
* CREATE_STAT_TABLE(id, stepId)
* ADD_STAT_TO_TABLE(id, stepId, name, value, isNameRawText, isValueRawText, isTotalRow, isStatValueTime, colourId)
* ADD_STAT_TABLE_TO_WALL(id, stepId)
* SHOW_STAT_WALL(id)
* CREATE_INCREMENTAL_CASH_ANIMATION(id, stepId)
* ADD_INCREMENTAL_CASH_WON_STEP(id, stepId, startDollars, finishDollars, topText, bottomText, rightHandStat, rightHandIcon, soundType)
* ADD_INCREMENTAL_CASH_ANIMATION_TO_WALL(id, stepId)
* ADD_JOB_POINTS_TO_WALL(id, points, xAlign)
* ADD_REP_POINTS_AND_RANK_BAR_TO_WALL(id, repPointsGained, startRepPoints, minRepPointsForRank, maxRepPointsForRank, currentRank, nextRank, rank1Txt, rank2Txt)
* PAUSE_BEFORE_PREVIOUS_LAYOUT()
* ADD_CASH_DEDUCTION(id, title, description, value)
* ADD_CASH_WON_TO_WALL(id, statLabel, finalValue, startValue, xAlign, isRawText)
* ADD_CASH_TO_WALL(id, value, xAlign)
* CLEANUP(id)
* createSequence(bgColour, sfxId, id)
* getLocalisedText(label)
* getColourFromId(id)

 HEIST_MP
^^^^^^^^^

* HEIST_MP()
* INITIALISE(mc)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* ADD_TXD_REF_RESPONSE(textureDict, uniqueID, success)
* DISPLAY_VIEW(viewIndex)
* HIGHLIGHT_ITEM(_itemIndex, _subItemIndex, leftArrow, rightArrow)
* HIGHLIGHT_BUTTON_HACK()
* SET_DATA_SLOT(_viewIndex, _slotIndex)
* UPDATE_DATA_SLOT(_viewIndex, _slotIndex)
* SHOW_VIEW(_viewIndex, _show)
* CLEAR_VIEW()
* SET_LABELS(_theHeist, _launchButton, _theTake, _thePlan, _total, _playerCut, _role, _cut, _status, _outfit)
* ADD_CREW_MEMBER(_playerSlot, _playerName, _rank, _portrait, _role, _roleIcon, _status, _statusIcon, _cutCash, _cutPercentage, _gangIconEnum, _codename, _outfit, _numPlayers)
* UPDATE_CREW_MEMBER(_playerSlot, _playerName, _rank, _portrait, _role, _roleIcon, _status, _statusIcon, _cutCash, _cutPercentage, _gangIconEnum, _codename, _outfit, _numPlayers, _headsetIcon, _invalidSelection)
* BLANK_CREW_MEMBER(_playerSlot)
* SET_PLAYERLIST_ICON(_slotIndex, _headsetIcon)
* repositionLaunchButton()
* SET_HEIST_NAME(_heistName, _info, _team, _title)
* UPDATE_HEIST_NAME(_heistName, _info, _team, _title)
* repositionHeistNameTitle(viewIndex)
* ADD_LAUNCH_BUTTON()
* LAUNCH_BUTTON_VISIBLE(_vis)
* LAUNCH_BUTTON_ENABLED(_enabled)
* LAUNCH_BUTTON_HIGHLIGHTED(_highlighted)
* SET_LAUNCH_BUTTON_COLOUR(hudColour)
* SET_LEADER_COST(message, value)
* formatAmount(value)
* ADD_PIECHART(_potentialTake, _player1Percent, _player2Percent, _player3Percent, _player4Percent, _pot)
* UPDATE_PIECHART(_potentialTake, _player1Percent, _player2Percent, _player3Percent, _player4Percent, _pot)
* ADD_TODO_LIST()
* UPDATE_TODO_LIST()
* GET_TODO_ITEM_LINE_COUNT(itemIndex)
* ADD_PLAYERCARD(_playerSlot, _playerName, _rank, _role, _portrait, _PlaneBool, _HeliBool, _BoatBool, _CarBool, kdRatio, title, status, stat1, stat2, stat3, stat4, stat5, stat6, stat7)
* UPDATE_PLAYERCARD(_playerSlot, _playerName, _rank, _role, _portrait, _PlaneBool, _HeliBool, _BoatBool, _CarBool, kdRatio, title, status, stat1, stat2, stat3, stat4, stat5, stat6, stat7)
* BLANK_PLAYERCARD(_playerSlot)
* ADD_PLAYERCARD_MEDALS(_playerSlot, _medal1, _medal2, _medal3, _medal4, _medal5, _medal6)
* ADD_PREVIEW(_slot, _title1, _txn)
* UPDATE_PREVIEW(_slot, _title1, _txn)
* BLANK_PREVIEW()
* ADD_PLANNING_SLOT(_itemSlot, _txd, _title, _txn1, _imageName1, _txn2, _imageName2, _txn3, _imageName3, _completed, _available, _highlight, _fadeInCross)
* UPDATE_PLANNING_SLOT(_itemSlot, _txd, _title, _txn1, _imageName1, _txn2, _imageName2, _txn3, _imageName3, _completed, _available, _highlight, _fadeInCross)
* getNumOfPlanningSlots()
* BLANK_PLANNING_SLOT(_itemSlot)
* SET_STRAND_BOARD_TITLE(_title)
* ADD_STRAND_SLOT(_itemSlot, _txd, _title, _description, _txn1, _completed, _available, _cost)
* UPDATE_STRAND_SLOT(_itemSlot, _txd, _title, _description, _txn1, _completed, _available, _cost)
* getNumOfStrandSlots()
* BLANK_STRAND_SLOT(_itemSlot)
* HIDE_PLANNING_SLOT(_itemSlot)
* SHOW_PLANNING_SLOT(_itemSlot)
* UPDATE_PLANNING_SLOT_LEFT(_itemSlot)
* UPDATE_PLANNING_SLOT_RIGHT(_itemSlot)
* UPDATE_PLANNING_SLOT_RIGHT_MEDAL(_itemSlot)
* SHOW_PLANNING_IMAGES(bool)
* INITIALISE_HEISTBOARD()
* INITIALISE_PLANNINGBOARD()
* INITIALISE_STRANDBOARD()
* SHOW_HEISTBOARD()
* SHOW_PLANNINGBOARD()
* SHOW_STRANDBOARD()
* SHOW_ALL_TEXT()
* HIDE_ALL_TEXT()
* CLEANUP()

 HEIST_PRE
^^^^^^^^^^

* HEIST_PRE()
* INITIALISE(mc)

 HEISTMAP_MP
^^^^^^^^^^^^

* HEISTMAP_MP()
* INITIALISE(mc)
* RESET_ALL_DEPTHS()
* BRING_PIN_TO_FRONT(pinEnum)
* ADD_PIN(pinEnum, iconEnum, Xpos, Ypos, Scale, colR, colG, colB, colA)
* REMOVE_PIN(pinEnum)
* REMOVE_ALL_PINS()
* COLOUR_PIN(pinEnum, colR, colG, colB, colA, iconEnum)
* BRING_AREA_TO_FRONT(areaEnum)
* ADD_AREA(areaEnum, Xpos, Ypos, Diameter, colR, colG, colB, colA)
* REMOVE_AREA(areaEnum)
* REMOVE_ALL_AREAS()
* COLOUR_AREA(areaEnum, colR, colG, colB, colA)
* BRING_TEXT_TO_FRONT(textEnum)
* ADD_TEXT(textEnum, textString, Xpos, Ypos, textAngle, fontSize, textWidth, textAlpha, dropShadow)
* REMOVE_TEXT(textEnum)
* REMOVE_ALL_TEXT()
* COLOUR_TEXT(textEnum, colR, colG, colB, colA)
* HIDE_ALL_TEXT()
* SHOW_ALL_TEXT()
* BRING_POSTIT_TO_FRONT(postitEnum)
* ADD_POSTIT(postitEnum, textNumber, Xpos, Ypos)
* REMOVE_POSTIT(postitEnum)
* REMOVE_ALL_POSTITS()
* COLOUR_POSTIT(postitEnum, colR, colG, colB, colA)
* SCALE_POSTIT(postitEnum, scale)
* BRING_ARROW_TO_FRONT(arrowEnum)
* ADD_ARROW(arrowEnum, fromX, fromY, toX, toY, curve)
* REMOVE_ARROW(arrowEnum)
* REMOVE_ALL_ARROWS()
* COLOUR_ARROW(arrowEnum, colR, colG, colB, colA)
* BRING_HIGHLIGHT_TO_FRONT(highlightEnum)
* ADD_HIGHLIGHT(highlightEnum, Xpos, Ypos, Size, colR, colG, colB, colA)
* REMOVE_HIGHLIGHT(highlightEnum)
* REMOVE_ALL_HIGHLIGHTS()
* COLOUR_HIGHLIGHT(highlightEnum, colR, colG, colB, colA)
* ZOOM_MAP(zoom)
* CLEANUP()
* checkIfMapIsStillDrawing()
* executeZoomTrue()

 INTERIORS
^^^^^^^^^^

* INTERIORS(TIMELINE)

 minigames
==========

 AXE_OF_FURY
^^^^^^^^^^^^

* AXE_OF_FURY()
* initialise(mc)
* reset()
* updateMeterFlash(frameCountdown)
* SHOW()
* HIDE()
* SET_SCREEN_POSITION(xNorm, yNorm)
* SET_BUTTON_VISIBLE(isVisible)
* FLASH_BUTTON()
* SET_METER_BAR_LINE_VISIBLE(isVisible)
* SET_METER_BAR_ICON_VISIBLE(isVisible)
* SET_METER_BAR_VALUE(value)
* SET_METER_FILL_VALUE(value)
* FLASH_METER()
* SET_IS_KEYBOARD_CONTROL(isKeyboard)

 DANCER
^^^^^^^

* DANCER()
* initialise(mc)
* SET_SCREEN_POSITION(xNorm, yNorm)
* SET_IS_MOUSE_CONTROL(isMouse)
* SET_IS_LT_CONTROL(isLT)
* SET_LEVEL(level)
* MUSIC_BEAT()
* PLAYER_BEAT(isAGoodBeat)
* FLASH_ICON()
* PULSE_ICON()
* SET_METER(normValue)
* SET_METER_IS_RED(isRed)
* delegate(scope, method)
* update()
* setColour(colour)
* fadeColour()
* setFlash(colour)
* fadeFlash()
* setPulse()
* fadePulse()
* setIcon()

 DARTS_SCOREBOARD
^^^^^^^^^^^^^^^^^

* DARTS_SCOREBOARD()
* INITIALISE(mc)
* debug()
* SET_PLAYER_HIGHLIGHT(who)
* SET_CREW_TAG(player, tag, isPrivate)
* SET_PLAYER_SETS_AND_LEGS(p1Sets, p2Sets, p1Legs, p2Legs)
* SET_DARTS_PLAYER_NAMES(playerOne, playerTwo)
* ADD_DARTS_SCORE(playerID, score)
* CLEAR_DARTBOARD()
* CLEAR_SCORES(playerID)
* resetRow(playerID)

 DARTS_SCOREBOARD_BIKER
^^^^^^^^^^^^^^^^^^^^^^^

* DARTS_SCOREBOARD_BIKER()
* INITIALISE(mc)
* debug()
* SET_PLAYER_HIGHLIGHT(who)
* SET_CREW_TAG(player, tag, isPrivate)
* SET_PLAYER_SETS_AND_LEGS(p1Sets, p2Sets, p1Legs, p2Legs)
* SET_DARTS_PLAYER_NAMES(playerOne, playerTwo)
* ADD_DARTS_SCORE(playerID, score)
* CLEAR_DARTBOARD()
* CLEAR_SCORES(playerID)
* resetRow(playerID)

 DONT_CROSS_THE_LINE
^^^^^^^^^^^^^^^^^^^^

* DONT_CROSS_THE_LINE()
* initialise(mc)
* SHOW_LOADING_SCREEN()
* HIDE_LOADING_SCREEN()
* SET_CENTRAL_MESSAGE(message, hudColourEnum, effectEnum, secondaryMessage, secondaryHudColourEnum)
* CLEAR_CENTRAL_MESSAGE()
* INIT_LOBBY(message, hudColourEnum, player1Txd, player1GamerTag, player2Txd, player2GamerTag, player3Txd, player3GamerTag, player4Txd, player4GamerTag, localPlayerIndex)
* UPDATE_LOBBY(player1Action, player2Action, player3Action, player4Action)
* HIDE_LOBBY()
* SHOW_HUD(player1Score, player1Txd, player1GamerTag, player2Score, player2Txd, player2GamerTag, player3Score, player3Txd, player3GamerTag, player4Score, player4Txd, player4GamerTag, localPlayerIndex)
* HIDE_HUD()
* SET_MICS(player1Mic, player2Mic, player3Mic, player4Mic)
* initLobbyPlayer(mc, txd, gamerTag, isLocal)
* updateLobbyPlayer(mc, action)
* initHUDPlayer(mc, score, txd, gamerTag, isLocal)
* addImage(txd, id, imageTextField)
* TXD_HAS_LOADED(txd)
* clearImageQueue()
* displayImage(txd, id, imageTextField)
* setOutlineText(container, text, hudColourEnum, shrink)
* hudColourIsValid(hudColour)
* setMic(mc, iconEnum)

 GOLF
^^^^^

* GOLF()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* SET_DISPLAY(state)
* SET_HOLE_DISPLAY(hole, par, dist)
* SET_SWING_DISPLAY(state, lie, lieEnum, wind, windDirection, club, clubEnum, swing, swingChangable, spin, spinPower, spinDirection, shotStr)
* _contentEnterFrame()
* _spinDisplay()
* SET_PLAYERCARD_SLOT(id, state, name, crewTag, txd, txn, ballColor, score, scoreColor)
* SET_PLAYERCARD_HEADSET(id, headsetEnum)
* CLEAR_PLAYERCARD_SLOT(id)
* updatePlayerCardDisplay()
* SET_SCOREBOARD_TITLE(title, holeLabel, parLabel, scoreLabel, holeInOne, underPar, overPar)
* COURSE_PAR()
* SET_SCOREBOARD_SLOT(id, state, name, crewTag, readyStr, ballColor, score, scoreColor, c0, c1, c2, c3, c4, c5, c6, c7, c8)
* CLEAR_SCOREBOARD_SLOT(id)
* updateScoreboardDisplay()
* ADD_TXD_REF_RESPONSE(txd, strRef, success)
* SWING_METER_SET_MARKER(hVisible, hPosition, vVisibile, vPosition)
* SWING_METER_SET_APEX_MARKER(hVisible, hPosition, vVisibile, vPosition)
* SWING_METER_SET_TARGET(span, position)
* SWING_METER_SET_TARGET_COLOR(r, g, b, a)
* SWING_METER_SET_FILL(span, state, fromTop)
* SWING_METER_POSITION(x, y, center)
* SWING_METER_SCALE(w, h)
* SWING_METER_IS_TRANSITIOING()
* SWING_METER_TRANSITION_IN()
* SWING_METER_TRANSITION_OUT(duration)

 GOLF_FLOATING_UI
^^^^^^^^^^^^^^^^^

* GOLF_FLOATING_UI()
* INITIALISE(mc)
* SET_SWING_DISTANCE(label, value, arrow)
* SET_PIN_DISTANCE(label, value, arrow)
* SET_HEIGHT(label, value, arrow)
* SET_STRENGTH(label, value, arrow)
* UPDATE_SLOT(id, label, value, arrow)
* TRANSITION_IN(duration)
* TRANSITION_OUT(duration)
* _handleTransitionOutComplete()

 HORSE_RACING_CONSOLE
^^^^^^^^^^^^^^^^^^^^^

* HORSE_RACING_CONSOLE()
* initialise(mc)
* SET_INPUT_EVENT(inputID)
* SET_ANALOG_STICK_INPUT(isLeftStick, x, y, isMouseWheel)
* SET_CURSOR_SPEED(speed)
* SET_MOUSE_INPUT(x, y)
* ENABLE_NAVIGATION()
* DISABLE_NAVIGATION()
* GET_CURRENT_SELECTION()
* SHOW_SCREEN(screenID)
* GET_CURRENT_SCREEN_ID()
* SET_RACE_TYPE(isSingleRace)
* SET_HORSE(number, name, odds, primaryColour, secondaryColour, horseColour, maneColour)
* SET_COUNTDOWN(secondsRemaining)
* SET_BETTING_VALUES(selectedHorse, betAmount, chips, payout, isMain)
* SET_BETTING_ENABLED(isEnabled)
* SET_MAIN_EVENT_IN_PROGRESS(isInProgress)
* START_RACE(duration, seed, firstHorse, secondHorse, thirdHorse, fourthHorse, fifthHorse, sixthHorse, offset)
* GET_RACE_IS_COMPLETE()
* SHOW_ERROR(title, message)
* GET_HORSE_POSITIONS()
* showScreen(screenID)
* updateButtons()
* TXD_HAS_LOADED(txd, success, id)
* formatPercentage(value)
* formatNumber(value)
* formatTime(seconds)
* truncate(tf, txt, autoSize, letterSpacing)
* playSound(soundName, soundSet)

 HORSE_RACING_WALL
^^^^^^^^^^^^^^^^^^

* HORSE_RACING_WALL()
* HORSE_RACING()
* initialise(mc)
* SHOW_SCREEN(screenID)
* GET_CURRENT_SCREEN_ID()
* SET_HORSE(number, name, odds, primaryColour, secondaryColour, horseColour, maneColour)
* SET_DETAIL_HORSE(number)
* SET_COUNTDOWN(secondsRemaining)
* ADD_PLAYER(gamertag, horse, bet)
* REMOVE_PLAYER(gamertag)
* SET_PLAYER_RESULT(gamertag, result)
* CLEAR_ALL_PLAYERS()
* START_RACE(duration, seed, firstHorse, secondHorse, thirdHorse, fourthHorse, fifthHorse, sixthHorse, offset, sync)
* GET_RACE_IS_COMPLETE()
* SHOW_ERROR(title, message)
* GET_HORSE_POSITIONS()
* getPlayerIndex(gamertag)
* showScreen(screenID)
* TXD_HAS_LOADED(txd, success, id)
* formatPercentage(value)
* formatNumber(value)
* formatTime(seconds)
* truncate(tf, txt, autoSize, letterSpacing)
* resizeAsianText(tf)
* playSound(soundName, soundSet)

 SC_LEADERBOARD
^^^^^^^^^^^^^^^

* SC_LEADERBOARD()
* SCLeaderboard()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* debugMP()
* SET_DISPLAY_TYPE()
* SET_MULTIPLAYER_TITLE(title)
* SET_TITLE(title)
* SET_SLOT(id, state)
* onSlotMouseEvent(evtType, targetMC, args)
* SET_SLOT_STATE(id, state)
* SET_SLOT_HOVER(id, isVisible)
* CLEAR_SLOT(id)
* CLEAR_ALL_SLOTS()
* canUseFixedWidthNumbers(str, validChars)
* updateDisplay()

 SPIN_THE_WHEEL
^^^^^^^^^^^^^^^

* SPIN_THE_WHEEL()
* initialise(mc)
* SET_WHEEL_STYLE(wheelType, numSegments, isSpectatorWheel)
* SET_SEGMENT(index, type, value)
* SPIN_WHEEL(targetSegment, numFullSpins, totalDuration, winPauseDuration, winIcon, winMessage)
* SET_LABEL_TEXT(text, isRedText)

 TENNIS
^^^^^^^

* TENNIS()
* INITIALISE(mc)
* initScreenLayout()
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isHiDef, _isAsian)
* DISPLAY_SCOREBOARD(value)
* DISPLAY_PLAYER_CARD(value)
* SET_SCOREBOARD_TITLE(title, column0)
* SET_SCOREBOARD_SLOT(id, isMP, name, crewTag, isSelected, column0)
* SET_PLAYERCARD_TITLE(column0)
* SET_PLAYERCARD_SLOT(id, isMP, name, crewTag, isSelected, txd, txn, column0)
* SET_PLAYERCARD_HEADSET(id, headsetEnum)
* ADD_TXD_REF_RESPONSE(txd, strRef, success)
* SWING_METER_SET_MARKER(hVisible, hPosition, vVisibile, vPosition)
* SWING_METER_SET_APEX_MARKER(hVisible, hPosition, vVisibile, vPosition)
* SWING_METER_SET_TARGET(span, position)
* SWING_METER_SET_TARGET_COLOR(r, g, b, a)
* SWING_METER_SET_FILL(span, state, fromTop)
* SWING_METER_POSITION(x, y, center)
* SWING_METER_SCALE(w, h)
* SWING_METER_IS_TRANSITIOING()
* SWING_METER_TRANSITION_IN()
* SWING_METER_TRANSITION_OUT(duration)

 minimap
========

 FOG_MC
^^^^^^^


 GOLF_COURSE
^^^^^^^^^^^^

* GOLF_COURSE(TIMELINE)

 GREEN_AND_FRIENDLY
^^^^^^^^^^^^^^^^^^^

* GREEN_AND_FRIENDLY()

 GREEN_AND_NET_PLAYER1
^^^^^^^^^^^^^^^^^^^^^^

* GREEN_AND_NET_PLAYER1()

 GREEN_AND_NET_PLAYER2
^^^^^^^^^^^^^^^^^^^^^^

* GREEN_AND_NET_PLAYER2()

 GREEN_AND_NET_PLAYER3
^^^^^^^^^^^^^^^^^^^^^^

* GREEN_AND_NET_PLAYER3()

 MINIMAP
^^^^^^^^

* MINIMAP(mc)
* REGISTER_HEALTH_ARMOUR(_healthContainer)
* INITIALISE()
* READY()
* SETUP_HEALTH_ARMOUR(healthType)
* rescaleAllBars()
* SET_PLAYER_HEALTH(newHealthValue, wasAdded, capacity, showDamage)
* FLASH_HEALTH_BAR(vis)
* flashHealthBarRed()
* removeRedHealthBar()
* SET_PLAYER_ARMOUR(newArmourValue, wasAdded, capacity)
* SET_AIR_BAR(newAirValue)
* HIDE_AIR_BAR()
* SET_ABILITY_BAR(newAbilityValue, wasAdded, capacity)
* SET_ABILITY_BAR_GLOW(isVisible)
* SET_ABILITY_BAR_GLOW_POINT(isVisible, isMax)
* SET_ABILITY_BAR_VISIBLE(isVisible)
* MULTIPLAYER_IS_ACTIVE(isMP, allowAbilityBar)
* SET_ABILITY_BAR_VISIBILITY_IN_MULTIPLAYER(isVisible)
* SET_HEALTH_DAMAGE_VISIBLE(vis, fadeTime)
* FLASH_MINIMAP(eFlashColour)
* SET_MASK(maskMC)
* MOVE_MAPMASKSQUARE(isVisible)
* SET_COLOUR(mc, r, g, b, a)
* SET_RADIUS_BLIP_COLOUR(mc, r, g, b, a)
* SHOW_CROSSHAIR(vis)
* TOGGLE_BLIP_LABEL(mc, str)
* SET_BLIP_DEATH(mc, isDead)
* SET_BLIP_LABEL(mc, str, labelScale)
* REMOVE_BLIP_LABEL(mc)
* START_BLIP_FLASHING(mc, blinkSpeed)
* STOP_BLIP_FLASHING(mc)
* REMOVE_BLIP(mc)
* BLINK_ABILITY_BAR(millisecondsToFlash)
* blinkOn(blinkRate, blinkRemaining)
* blinkOff(blinkRate, blinkRemaining)
* FLASH_ABILITY_BAR(params)
* flashAbilityOn(blinkSpeed)
* flashAbilityOff(blinkSpeed)
* START_FLASHING_ABILITY(blinkSpeed)
* STOP_FLASHING_ABILITY()
* flashAbilityGlowOn(blinkSpeed)
* flashAbilityGlowOff(blinkSpeed)
* STOP_FLASHING_ABILITYGLOW()
* flashOn(mc, blinkSpeed)
* flashOff(mc, blinkSpeed)
* SET_WANTED_LEVEL(circle, wantedLevel, radius)
* GET_ASSET_ARRAY()
* GET_SIZE(mc)
* SET_HEALTH_ARMOUR_BAR_VISIBLE(_vis)
* SET_SATNAV_DIRECTION(iconEnum)
* SET_SATNAV_DISTANCE(distance, isMetric)
* HIDE_SATNAV()
* SHOW_SATNAV()
* SET_DEPTH(distanceToSurface, distanceToFloor, isMetric, warning)
* HIDE_DEPTH()
* SHOW_DEPTH()
* SHOW_SONAR_SWEEP(isVisible)
* formatDistance(distance, isMetric)
* HIDE_HEALTH_ARMOUR()
* SHOW_HEALTH_ARMOUR()
* SHOW_STALL_WARNING(_vis)
* FLASH_WANTED_OVERLAY()
* STOP_FLASHING_WANTED_OVERLAY()
* SHOW_YOKE(xFloat, yFloat, vis, alpha)
* REGISTER_TERRITORY(mc)
* SET_MP_PROPERTY_OWNER(propertyID, owner, owner2, owner3)
* CYCLE_GANG_COLOURS(mc, propertyID, currentOwner, ownerArray)

 MINIMAP_MAIN_MAP
^^^^^^^^^^^^^^^^^

* MINIMAP_MAIN_MAP(mc)
* REGISTER_MAP_LAYER(_MAP)
* REGISTER_ROADS_LAYER(_ROADS)
* hideALlComponents()
* TOGGLE_COMPONENT(component, visible, hudColour)
* debug(component, visible, hudColour)
* SHOW_AIRCRAFT_COMPONENTS(shouldBeVisible)
* SET_BITMAP_MAP_ON(txd, xpos, ypos)
* SET_BITMAP_MAP_OFF(txd)

 NET_PLAYER1_AND_NET_PLAYER2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* NET_PLAYER1_AND_NET_PLAYER2()

 NET_PLAYER1_AND_NET_PLAYER3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* NET_PLAYER1_AND_NET_PLAYER3()

 TXD_MC
^^^^^^^


 platform_pc
============

 GAMEPAD_CALIBRATION
^^^^^^^^^^^^^^^^^^^^

* GAMEPAD_CALIBRATION()
* INITIALISE(mc)
* SHOW_BUTTON(button, showButton, hidePrevious)
* BAR_POSITION(pos)
* SHOW_BAR(showBar)
* CONSTRUCT_STRING(button, startString, endString, prompt, clearOld, hasFill)
* SET_BUTTON_PRESS_STATE(isPressed, prompt)
* END_CALIBRATION()

 LANGUAGE_SELECT
^^^^^^^^^^^^^^^^

* LANGUAGE_SELECT()
* INITIALISE(mc)
* SET_DISPLAY_CONFIG(_screenWidthPixels, _screenHeightPixels, _safeTopPercent, _safeBottomPercent, _safeLeftPercent, _safeRightPercent, _isWideScreen, _isCircleAccept, _isAsian)
* GET_CURRENT_SELECTION()
* SET_INPUT_EVENT(direction)
* clearLanguages()
* SET_LANGUAGES()
* SET_HIGHLIGHT()

 PC_KEY
^^^^^^^

* PC_KEY()

 TATTOO_KEYS
^^^^^^^^^^^^

* TATTOO_KEYS()
* INITIALISE(mc)
* ADD_BUTTON(whichButton)
* angleIsCloseTo(angleA, angleB, maxDelta)
* FADE_OUT_OLD_BUTTON()
* REORDER_BUTTONS_ARRAY()
* SET_STICK_POINTER_ANGLE(arAngle, color)
* HIDE_STICK_POINTER()

 TEXTBTN_996
^^^^^^^^^^^^


 TEXTBTN_997
^^^^^^^^^^^^


 TEXTBTN_999
^^^^^^^^^^^^


 web
====

 FORECLOSURES_MAZE_D_BANK_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* FORECLOSURES_MAZE_D_BANK_COM()
* POPULATE_TEXT(pageName, searchArgs, newPage)
* displayPage(pageName)
* CLEANUP()
* setSelectedClubhouse(id)
* getSelectedClubhouse()
* getClubhouseByID(id)
* getSelectedClubhouseType()
* dispatchPlayerSelections()
* updateNewlyPurchasedClubhouse()
* setSelectedBunker(id)
* getSelectedBunker()
* getBunkerByID(id)
* dispatchPlayerBunkerSelections()
* updateNewlyPurchasedBunker()
* setSelectedHangar(id)
* getSelectedHangar()
* getHangarByID(id)
* dispatchPlayerHangarSelections()
* updateNewlyPurchasedHangar()
* setSelectedBase(id)
* getSelectedBase()
* getBaseByID(id)
* dispatchPlayerBaseSelections()
* updateNewlyPurchasedBase()
* setSelectedNightclub(id)
* getSelectedNightclub()
* getNightclubByID(id)
* dispatchPlayerNightclubSelections()
* updateNewlyPurchasedNightclub()
* setSelectedArcade(id)
* getSelectedArcade()
* getArcadeByID(id)
* dispatchPlayerArcadeSelections()
* updateNewlyPurchasedArcade()
* showTradeInAlert()
* INITIALISE(mc)
* setPage(pageName, PageClass)

 FORECLOSURES_MAZE_D_BANK_COM_WRAPPER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* FORECLOSURES_MAZE_D_BANK_COM_WRAPPER()
* TXD_HAS_LOADED(txd, success, id)
* DISABLE_VIDEO(isDisabled)
* goToAnchor(link)
* handleLB()
* handleRB()
* handleLT()
* handleRT()
* handleLTRelease()
* handleRTRelease()
* handleAnalogStickInput(isLeftStick, x, y, isScrollWheel)
* handleMouseClick(inputIsMouseClick)
* handleMouseRelease()

 FORMAT_COLUMN
^^^^^^^^^^^^^^

* FORMAT_COLUMN()

 GENERIC_WEBSITE_SCRIPT
^^^^^^^^^^^^^^^^^^^^^^^

* GENERIC_WEBSITE_SCRIPT()
* READY()
* POPULATE_TEXT(pageName)

 MYSTOCKS_BUTTON
^^^^^^^^^^^^^^^^


 STOCKLIST_BUTTON
^^^^^^^^^^^^^^^^^


 TICKERTAPE
^^^^^^^^^^^

* TICKERTAPE()
* SET_TICKER_TEXT(scrollSpeed, displyText)
* Scroll(speed)

 WEB_BROWSER
^^^^^^^^^^^^

* WEB_BROWSER()
* INITIALISE(mc)
* getConfig()
* setFlags(flagIndex, flagValue)
* setScrollBarVisibility(isVisible)
* SCROLL_WEBPAGE_PIXELS(amount)
* URL_HAS_SUBDOMAIN(inputString)
* PARSE_FILENAME_TO_TEXT(inputString)
* PARSE_TEXT_TO_FILENAME(inputString)
* UPDATE_TOOLBAR_BUTTONS()
* GO_FORWARD()
* GO_BACK()
* ADD_URL_ARGS_TO_HISTORY(searchResults)
* UPDATE_HISTORY_AND_ADDRESS(website)
* buttonActionSetHistory()
* buttonActionSetBrowserList(buttonIndex)
* setCloseBrowserFlag()
* GO_TO_WEBPAGE_ID(siteId, pageId)
* GO_TO_WEBPAGE(websiteString)
* SHOW_ERROR_PAGE()
* SHOW_DATA_EXPIRED_ERROR(_website)
* INITIALISE_WEBSITE()
* updateAddressBarText(url)
* UPDATE_TEXT(newPage)
* RESIZE_WEBSITE()
* IS_SITE_DYNAMIC()
* REQUEST_STREAM(uid, filename)
* pingTimer()
* STREAM_RESPONSE_FAILED(uid)
* STREAM_RESPONSE(uid, fileToLoad)
* LOAD_CLIP(params, fileToLoad)
* onLoadInit(target_mc)
* onLoadError(target_mc)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* TXD_ALREADY_LOADED(textureDict, uniqueID)
* REMOVE_CHILD_MOVIE(whichMC)
* REQUEST_REMOVE_WEBSITE(whichMC)
* SHUTDOWN_MOVIE()
* SET_CURRENT_OBJECT_TYPE(currentObj)
* SET_CURSOR_STATE(state)
* GET_CURSOR_STATE()
* SHOW_CURSOR(vis)
* HIDE_CURSOR()
* setCursorBusy()
* setCursorInvisabile()
* SHOW_BACKGROUND(vis)
* createKeyboard(focus)
* setKeyboard(keyboardType)
* SHOW_KEYBOARD()
* HIDE_KEYBOARD()
* SET_PC_KEY(_key)
* ENTER_BROWSER_TEXT(_key)
* ENTER_TEXT(inputString, doNotEcho)
* ALIGN_TEXTFIELD(targetTextfield)
* ALIGN_TOOLBAR_TEXTFIELDS()
* MAKE_LIST(listArray)
* REMOVE_LIST()
* SEARCH_ARRAY(arrayData, stringToFind)
* handleAnalogInput()
* SET_INPUT_EVENT(direction)
* SET_INPUT_RELEASE_EVENT(direction)
* SET_INPUT_SELECT(inputIsMouseClick)
* SET_ANALOG_STICK_INPUT(isLeftStick, mouseX, mouseY, isScrollWheel)
* SET_MOUSE_INPUT(mouseX, mouseY)
* tab_buttons(direction)
* getMinBounds(targetMC)
* getMaxBounds(targetMC)
* testDirection(direction, butX, butY, curX, curY)
* endCursorSnap(buttonMC)
* getAngle(x1, y1, x2, y2)
* getRelativeAngle(x1, y1, x2, y2, dir)
* getDistance(x1, y1, x2, y2)
* hitTestButtons(x, y)
* hitTestKeyboardButtons(x, y)
* checkButtonsTest(buttonlist, x, y)
* checkButtonsTestIncludeMask(buttonlist, x, y)
* SET_BUTTON_MASK(buttonMask)
* processButton(targetButton)
* SET_PAGE_BUTTONS(_dataTextScope)
* setButtonsInitialState()
* cleanupButtons()
* SET_ACTIVE_BUTTON(currentButton, currentButtonTarget)
* setButtonState(target, state)
* getTextLinkOnColour(target)
* getTextLinkOffColour(target)
* remove_tween(removeTween, commandString)
* SET_MULTIPLAYER(_multiplayer)
* SUPRESS_HISTORY(_suppressBackButton)
* SET_TITLEBAR_TEXT(titlebarText, hexColour)
* SET_BROWSER_CURSOR_SPEED_MODIFIER(newSpeed)
* IS_JAPANESE(_isJapanese)
* SET_BROWSER_SKIN(skinEnum)
* SET_PRICES(slotID, price, secondaryPrice, reductionType, salePrice, secondarySalePrice, award, price1Unlocked, price2Unlocked)
* SET_RANKS(slotID, rank, current)
* DISABLE_VIDEO(disableVideo)
* SET_MOVIECLIP_IS_VISIBLE(isVisible, instanceEnum)
* PROXY_FUNCTION()
* SET_WIDESCREEN(isWideScreen)
* GET_SITE_ID()
* GET_PAGE_ID()
* GET_CURRENT_WEBSITE()
* SET_DATA_SLOT(slotID)
* APPEND_DATA_SLOT(slotID)
* APPEND_YACHT_DATA_SLOT(slotID)
* APPEND_OFFICE_DATA_SLOT(slotID)
* SET_DATA_SLOT_EMPTY()
* SET_TICKERTAPE(speed, name)
* GET_CURRENT_OBJECT_TYPE()
* GET_CURRENT_SELECTION()
* SET_CURRENT_SELECTION(newCurrentSelection)
* GET_CURRENT_ROLLOVER()
* IS_KEYBOARD_ACTIVE()
* CREATE_HIGHLIGHT(targetSlot, colR, colG, colB, colA)
* CLEAR_HIGHLIGHTS()
* DISABLE_BUTTON(targetSlot, isDisabled)
* DISABLE_ALL_BUTTONS(hideButtons, supressHistory)
* ENABLE_ALL_BUTTONS()
* setTextWithTranslation(TF, label)

 WEB_BROWSER_PARENT
^^^^^^^^^^^^^^^^^^^

* WEB_BROWSER_PARENT()

 WWW_ACCEPT_D_THE_D_CHAOS_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_ACCEPT_D_THE_D_CHAOS_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_ARENAWAR_TV
^^^^^^^^^^^^^^^^

* WWW_ARENAWAR_TV()
* INITIALISE(mc)
* initVehicles()
* setPage(pageName, PageClass)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* displayPage(pageName)
* SET_PRICES(id, tradePrice, buyItNowPrice, a, tradeSalePrice, buyItNowSalePrice, b, tradePriceAvailable, buyItNowPriceAvailable)
* TXD_HAS_LOADED(txd, success, id)
* DISABLE_VIDEO(isDisabled)
* CLEANUP()
* goToAnchor(link)
* handleLB()
* handleRB()
* handleLT()
* handleRT()
* handleLTRelease()
* handleRTRelease()
* handleAnalogStickInput(isLeftStick, x, y, isScrollWheel)
* handleMouseClick(inputIsMouseClick)
* handleMouseRelease()
* getPropertyBaseCost(getSaleCost)
* getStyleCost(selection, getSaleCost)
* getGraphicsCost(selection, getSaleCost)
* getColourCost(selection, getSaleCost)
* getExpansionFloorB1Cost(selection, getSaleCost)
* getExpansionFloorB2Cost(selection, getSaleCost)
* getMechanicACost(getSaleCost)
* getMechanicBCost(getSaleCost)
* getPersonalQuartersCost(getSaleCost)
* dispatchPropertySelections()
* setPageHeight(height)

 WWW_BAWSAQ_COM
^^^^^^^^^^^^^^^

* WWW_BAWSAQ_COM()
* READY()
* UPDATE_TICKERTAPE(speed)
* SET_MOVIECLIP_VISIBILITY(isVisible, instanceEnum)
* PROXY_FUNCTION()
* SET_BAWSAQ_PLAYER_CASH()
* goToAnchor(AnchorLinkLetter)
* updateSortSlotArrow(sortId, userTriggered)
* removeTween()
* makeAnchorButtons(arrayIndex, numberOfEntries)
* doesInitialExist(str)
* POPULATE_TEXT(pageName)
* SET_NEW_PAGE_HEIGHT(data, minHeight)
* customSortAlphaDescending(a, b)
* customSortAlphaAscending(a, b)
* customSortNumberDescending(a, b)
* customSortNumberAscending(a, b)
* MAKE_STOCK_LIST(indexStart, dataLength, stocks)
* UPDATE_FIXED_STOCK_LIST(indexStart, listItem)
* ADD_TEXT(numberOfSlots)
* TINT_AND_ADD_SYMBOLS()
* setAndPositionLogo(companyAbv)
* set_price_text(TF, price)

 WWW_BENNYSORIGINALMOTORWORKS_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_BENNYSORIGINALMOTORWORKS_COM()
* INITIALISE(mc)
* filterVehicles()
* setCommonPageIDs()
* DISABLE_VIDEO(videoDisabled)
* TXD_HAS_LOADED(txd, success, id)
* SET_PRICES(id, price, secondaryPrice, reductionType, salePrice, secondarySalePrice, award)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* goToAnchor(link)
* initHomePage(newPage)
* initHomeButton(button, titleLabel, descriptionLabel)
* addHomePageImage(vehicle, container)
* initShowroomPage(newPage)
* setShowroomCar(index)
* setShowroomImage(index)
* addShowroomImage(vehicle, container)
* initStockPage(newPage)
* playWipeAnimation()
* initFindUsPage(newPage)
* initDetailsPage(pageName, newPage)
* initPurchaseButtons(page, numOptions, maxWidth)
* initStats(page)
* setStatLine(txt, label, bar, value)
* initPurchasePage(newPage)
* initOutcomePage(headerText, bodyText, soldLabel)
* initTopMenu(page, selected)
* initMenuButton(button, label, isSelected, widths, showStar)
* displayImage(vehicle, container)
* initVehicleButtons(page, yOffset)
* initVehicleButton(vehicle, container, x, y)
* initOptions(page)
* updateBackground(contentItem, page)

 WWW_BLEETER_BIZ
^^^^^^^^^^^^^^^^

* WWW_BLEETER_BIZ()
* READY()
* makeAnchorButtons(buttonsArray)
* goToAnchor(AnchorLinkLetter)
* makeBleetList()
* findCharPic(stringToFind)
* makeTrendingBleets()
* POPULATE_TEXT(pageName)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* CLEANUP()

 WWW_CASHFORDEADDREAMS_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_CASHFORDEADDREAMS_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_CLASSICVINEWOOD_COM
^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_CLASSICVINEWOOD_COM()
* READY()
* POPULATE_TEXT(pageName)

 WWW_CREDITCARDCONSOLIDATIONKINGS_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_CREDITCARDCONSOLIDATIONKINGS_COM()
* INITIALISE(mc)
* READY()
* goToAnchor(AnchorLink)
* _isTestComplete()
* POPULATE_TEXT(pageName)
* addCommas(val)

 WWW_CULTSTOPPERS_COM
^^^^^^^^^^^^^^^^^^^^^


 WWW_DOCKTEASE_COM
^^^^^^^^^^^^^^^^^^

* WWW_DOCKTEASE_COM()
* filterVehicles()
* setCommonPageIDs()
* updateBackground(contentItem, page)
* initDetailsPage(pageName, newPage)
* initBuyItNowDetailsPage(id, currentVehicle, newPage, frame)
* initOutcomePage(headerText, bodyText, soldLabel, pauseBeforeShowing)
* addVehicleNames()
* getYachtFromId(id)
* goToAnchor(link)
* goToYachtStartAnchor(attribute)
* goToYachtModelAnchor(attribute)
* goToYachtFittingsAnchor(attribute)
* goToYachtLightingAnchor(attribute)
* goToYachtColourAnchor(attribute)
* goToYachtFlagAnchor(attribute)
* dispatchPlayerSelections()
* displayPage(pageName)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* initHomePage(newPage)
* updateHomePageBannerSlideshow(step)
* initYachtHomePage(newPage)
* getCheapestModification()
* getCheapestInitialPurchase()
* getLowestValueInArray(array, indexes)
* initYachtModelPage(newPage)
* initModelSlideshow()
* initModelDropDown(page)
* updateModelDropDown()
* updateModelText()
* getDisplayedModel()
* initYachtFittingsPage(newPage)
* initFittingsDropDown(page)
* updateFittingsDropDown()
* updateFittingsImage(page)
* initYachtLightingPage(newPage)
* initLightingButtons(page)
* updateLightingImage(page)
* initYachtColourPage(newPage)
* initColourButtons(page)
* updateColourImage(page)
* initYachtPersonalisePage(newPage)
* initFlagButtons(page)
* updateFlagImage(page)
* pollYachtNameChange(page)
* initYachtCheckoutPage(newPage)
* initSummaries(page)
* initSummaryItem(item, descriptionLabel, selectionLabel, imageID, imageTXD, itemModified)
* initTotalPrice(price)
* initYachtPurchasePage(newPage)
* initYachtPurchaseSuccessPage(newPage)
* initYachtPurchaseFailurePage(newPage)
* getCheapestValidPrice(price, salePrice)
* getTotalPrice(includeBaseCost)
* setLocalisedYachtText(tf, label, bold)
* initTabs(container, activeTab)
* initTab(tab, label, disabled, showTick, showCircle, x)
* updateTabs(page, noBluePanelAnimation)
* updateTab(tab, value, price, salePrice)
* updatePersonaliseTab(tab, value, flagPrice, namePrice, flagSalePrice, nameSalePrice)
* setTabDisabled(tab, isDisabled)
* initTextButton(button, label)
* initNextButton(button, isDisabled, heading)
* updateNextButton(button, isDisabled)
* initRoundedButton(button, label, textOnColour, textOffColour, backgroundColour, backgroundAlpha)
* setButtonDisabled(button, isDisabled)
* updateOptionButtons(page, buttonName, selectedIndex, numButtons, dataProviderIndex)
* initUpgradeItemCost(mc, cost, saleCost, nextButton)
* updateUpgradeItemCost(mc, cost, saleCost)
* updateUpgradeTotal(tf)
* initRebateSticker(page, isVisible, image)
* initSlideshow(numSlides, slideTXD, slideDisplay, imagePrefix, descriptionLabelPrefix, descriptionTextField, startIndex)
* updateSlideshow(step)
* updateYachtBackground(page)
* TXD_HAS_LOADED(txd, success, id)
* CLEANUP()
* disposeTweens()

 WWW_DOCKTEASE_COM_PARENT
^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_DOCKTEASE_COM_PARENT()
* handleLB()
* handleRB()

 WWW_DYNASTY8EXECUTIVEREALTY_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_DYNASTY8EXECUTIVEREALTY_COM()
* POPULATE_TEXT(pageName, searchArgs, newPage)
* rebuildOfficeData()
* displayPage(pageName)
* TXD_HAS_LOADED(txd, success, id)
* CLEANUP()
* goToAnchor(link)
* handleLB()
* handleRB()
* handleLT()
* handleRT()
* handleLTRelease()
* handleRTRelease()
* handleAnalogStickInput(isLeftStick, x, y, isScrollWheel)
* handleMouseClick(inputIsMouseClick)
* handleMouseRelease()
* setSelectedOffice(id)
* getSelectedOffice()
* getOfficeByID(id)
* hasOwnedGarage()
* dispatchPlayerSelections()
* dispatchPlayerGarageSelections()
* updateNewlyPurchasedOffice()
* INITIALISE(mc)
* setPage(pageName, PageClass)
* logState()

 WWW_DYNASTY8REALESTATE_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_DYNASTY8REALESTATE_COM()
* READY()
* goToAnchor(AnchorLink)
* addVisiblePropertyID(id)
* removeVisiblePropertyID(id)
* scrollListingsPage(_position, _instant)
* sortProperties()
* updateFilterButtons()
* zoomAndScrollToLastProperty()
* POPULATE_TEXT(_pageName, searchArgs, newPage)
* updateOptions(selectedIndex)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* formatAmount(value)
* randRange(min, max, blacklist)
* CLEANUP()

 WWW_EGOCHASERENERGYBAR_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_EGOCHASERENERGYBAR_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)
* scan_and_set_localised_text(scope)

 WWW_ELECTROTOKESYSTEM_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^


 WWW_ELITASTRAVEL_COM
^^^^^^^^^^^^^^^^^^^^^

* WWW_ELITASTRAVEL_COM()
* filterVehicles()
* setCommonPageIDs()
* updateBackground(contentItem, page)
* setOptionsButtons(selectedOption)
* initOutcomePage(headerText, bodyText, soldLabel, pauseBeforeShowing)
* goToAnchor(link)
* initDetailsPage(pageName, newPage)
* initBlimpPage(pageName, newPage)
* initPurchaseButtons(page, numOptions)
* initBuyItNowDetailsPage(id, currentVehicle, newPage, frame)
* displayImage(vehicle, container)

 WWW_EPSILONPROGRAM_COM
^^^^^^^^^^^^^^^^^^^^^^^

* WWW_EPSILONPROGRAM_COM()
* READY()
* PROXY_FUNCTION(_, _page)
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* displayPurchasedText()
* scan_and_set_localised_text(scope)
* set_localised_text(slotID, TF, TextLabel, setDataSlot, isHtml)
* set_robes_ad_text()
* SET_MOVIECLIP_VISIBILITY(isVisible, instanceEnum)

 WWW_EYEFIND_INFO
^^^^^^^^^^^^^^^^^

* WWW_EYEFIND_INFO()
* READY()
* updateWeatherWidget()
* generateRandomWebsites()
* urlHasSubdomain(url)
* goToAnchor(AnchorLinkString)
* POPULATE_TEXT(_pageName, searchArgs, newPage)
* formatSearchButtons(container)
* setDelayedText(TF, textStr, duration)
* showDelayedText(TF, textStr)
* clearSearchResults()
* setUpSponsoredAd(buttonID)
* doSearch(userSearchKeywords)
* loadButtonThumbnail(urlName, placeholder, textScopeSlot)
* loadNewsTexture(txd, placeholder)
* set_localised_text(slotID, TF, TextLabel, setDataSlot)
* getRandomWebsite()
* randRange(min, max)
* shuffleArray(source)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* updateBleets()
* moveFeaturedWebsites()
* UPDATE_TICKERTAPE(speed)
* CLEANUP()

 WWW_FAMEORSHAME_NET
^^^^^^^^^^^^^^^^^^^^

* WWW_FAMEORSHAME_NET()
* DISABLE_VIDEO(disableVideo)
* POPULATE_TEXT(pageName)

 WWW_FLEECA_COM
^^^^^^^^^^^^^^^

* WWW_FLEECA_COM()

 WWW_HUSHSMUSH_COM
^^^^^^^^^^^^^^^^^^

* WWW_HUSHSMUSH_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)
* scanAndSetupButtons()
* scan_and_set_localised_text(scope, noShrinkList)
* displayProfiles(scope, index)
* getProfileIndex(profileID)

 WWW_IWILLSURVIVEITALL_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_IWILLSURVIVEITALL_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)
* displayPurchasedText()
* addCommas(val)
* CLEANUP()

 WWW_JACKHOWITZER_COM
^^^^^^^^^^^^^^^^^^^^^

* WWW_JACKHOWITZER_COM()
* DISABLE_VIDEO(disableVideo)
* POPULATE_TEXT(pageName)

 WWW_JOCKCRANLEY_COM
^^^^^^^^^^^^^^^^^^^^

* WWW_JOCKCRANLEY_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)
* ADD_TEXT(numberOfSlots)

 WWW_KUNGFURAINBOWLAZERFORCE_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_KUNGFURAINBOWLAZERFORCE_COM()
* DISABLE_VIDEO(disableVideo)
* POPULATE_TEXT(pageName)

 WWW_LCN_D_EXCHANGE_COM
^^^^^^^^^^^^^^^^^^^^^^^

* WWW_LCN_D_EXCHANGE_COM()
* READY()
* UPDATE_TICKERTAPE(speed)
* SET_MOVIECLIP_VISIBILITY(isVisible, instanceEnum)
* PROXY_FUNCTION()
* SET_BAWSAQ_PLAYER_CASH()
* goToAnchor(AnchorLinkLetter)
* updateSortSlotArrow(sortId, userTriggered)
* removeTween()
* makeAnchorButtons(arrayIndex, numberOfEntries)
* doesInitialExist(str)
* POPULATE_TEXT(pageName)
* SET_NEW_PAGE_HEIGHT(data, minHeight)
* customSortAlphaDescending(a, b)
* customSortAlphaAscending(a, b)
* customSortNumberDescending(a, b)
* customSortNumberAscending(a, b)
* MAKE_STOCK_LIST(indexStart, dataLength, stocks)
* UPDATE_FIXED_STOCK_LIST(indexStart, listItem)
* ADD_TEXT(numberOfSlots)
* TINT_AND_ADD_SYMBOLS()
* setAndPositionLogo(companyAbv)
* set_price_text(TF, price)
* setTextWithTranslation(TF, label)

 WWW_LEGENDARYMOTORSPORT_NET
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_LEGENDARYMOTORSPORT_NET()
* filterVehicles()
* setCommonPageIDs()
* updateBackground(contentItem, page)
* initHomePage(newPage)
* initDetailsPage(pageName, newPage)
* initStandardDetailsPage(pageName, newPage)
* initBuyItNowDetailsPage(id, currentVehicle, newPage, frame)
* initNormalPriceButtons(page, numOptions)
* initBuyItNowPriceButtons(page, numOptions)
* initStats(page)
* setStatLine(txt, label, bar, value)
* initOutcomePage(headerText, bodyText, soldLabel, pauseBeforeShowing)
* goToAnchor(link)
* setOptionsButtons(selectedOption)

 WWW_LEGENDARYMOTORSPORT_NET_WRAPPER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_LEGENDARYMOTORSPORT_NET_WRAPPER()

 WWW_LENNYAVERY_D_REALTY_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_LENNYAVERY_D_REALTY_COM()
* READY()
* goToAnchor(AnchorLink)
* TXD_HAS_LOADED(textureDict, success, uniqueID)
* onLoadError(target_mc)
* POPULATE_TEXT(_pageName)
* CLEANUP()
* createContentLOS_D_SANTOS()

 WWW_LIFEINVADER_COM
^^^^^^^^^^^^^^^^^^^^

* WWW_LIFEINVADER_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* setupProfileBox()
* updateSponsoredAds()
* makeLists()
* randRange(min, max)
* CLEANUP()

 WWW_MAZE_D_BANK_COM
^^^^^^^^^^^^^^^^^^^^

* WWW_MAZE_D_BANK_COM()

 WWW_MINISTERINMINUTES_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_MINISTERINMINUTES_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_MONETARYSCIENCE_US
^^^^^^^^^^^^^^^^^^^^^^^

* WWW_MONETARYSCIENCE_US()
* READY()
* setupCalculator()
* doSelection(selection, direction)
* showResult()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_MYDIVINEWITHIN_COM
^^^^^^^^^^^^^^^^^^^^^^^

* WWW_MYDIVINEWITHIN_COM()
* READY()
* goToAnchor(AnchorLink)
* _isTestComplete()
* POPULATE_TEXT(pageName)
* scan_and_set_localised_text(scope)

 WWW_PANDMCYCLES_COM
^^^^^^^^^^^^^^^^^^^^

* WWW_PANDMCYCLES_COM()
* filterVehicles()
* setCommonPageIDs()
* updateBackground(contentItem, page)

 WWW_PRINCESSROBOTBUBBLEGUM_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


 WWW_PROPOSITION43_ORG
^^^^^^^^^^^^^^^^^^^^^^

* WWW_PROPOSITION43_ORG()
* READY()
* setupCreator()
* selectItem(mcName)
* checkSelections()
* showResult()
* setupButtons()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_PSYCHICSHOUTOUT_COM
^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_PSYCHICSHOUTOUT_COM()
* READY()
* setupChats()
* doSetup()
* writeLine()
* updateChatButton(buttonText, active)
* writeNextLine()
* setChatCharacter(char)
* setChatNumber(num)
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_REPUBLICANSPACERANGERS_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_REPUBLICANSPACERANGERS_COM()
* DISABLE_VIDEO(disableVideo)
* POPULATE_TEXT(pageName)

 WWW_RIGHTEOUSSLAUGHTER7_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_RIGHTEOUSSLAUGHTER7_COM()
* DISABLE_VIDEO(disableVideo)
* POPULATE_TEXT(pageName)

 WWW_SANANDREASDMV_COM
^^^^^^^^^^^^^^^^^^^^^^

* WWW_SANANDREASDMV_COM()
* READY()
* showDrivingTip()
* doQuestionnaireSetup(pb, pbi, aqc)
* updateQuestion(q, selected)
* checkAnswerStatus()
* setProceedButtonActive(active)
* checkAnswers()
* populateResults(title, desc)
* setupButtons()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_SAWATERANDPOWER_COM
^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_SAWATERANDPOWER_COM()
* DISABLE_VIDEO(disableVideo)
* POPULATE_TEXT(pageName)

 WWW_SIXFIGURETEMPS_COM
^^^^^^^^^^^^^^^^^^^^^^^


 WWW_SOUTHERNSANANDREASSUPERAUTOS_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_SOUTHERNSANANDREASSUPERAUTOS_COM()
* filterVehicles()
* setCommonPageIDs()
* setOptionsButtons(selectedOption)
* initOutcomePage(headerText, bodyText, soldLabel, pauseBeforeShowing)
* initStats(page)
* setStatLine(txt, label, bar, value)
* goToAnchor(link)
* initDetailsPage(pageName, newPage)
* initPartyBus()
* initPurchaseButtons(page, numOptions)
* initBuyItNowDetailsPage(id, currentVehicle, newPage, frame)
* initNormalPriceButtons(page, numOptions)
* initBuyItNowPriceButtons(page, numOptions)

 WWW_SOUTHERNSANANDREASSUPERAUTOS_COM_WRAPPER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_SOUTHERNSANANDREASSUPERAUTOS_COM_WRAPPER()

 WWW_SOUTHERNSANANDREASSUPERAUTOS_COM_WRAPPER_WRAPPER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_SOUTHERNSANANDREASSUPERAUTOS_COM_WRAPPER_WRAPPER()

 WWW_TACO_D_BOMB_COM
^^^^^^^^^^^^^^^^^^^^

* WWW_TACO_D_BOMB_COM()
* READY()
* setupProducts()
* showProduct(prevNext)
* createProduct(prodObject)
* cleanUpProduct()
* setupPhrases()
* showPhrase(prevNext)
* createPhrase(phraseObject)
* playPhrase()
* cleanUpPhrase()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_THEBANKOFLIBERTY_COM
^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_THEBANKOFLIBERTY_COM()

 WWW_THECHILDRENOFTHEMOUNTAIN_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_THECHILDRENOFTHEMOUNTAIN_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* gotoPage1()
* gotoStage2()
* gotoStage3()
* gotoStage4()
* gotoCertificate()
* setupHeader(scope)
* scan_and_set_localised_text(scope, noShrinkList)
* CLEANUP()
* setPage1Content(scope, status)
* initAnagrams(scope)
* setupAnagramResult(scope)
* updateAnagramTimer()
* updateLetter(index)
* anagramDone()
* showLoseScreen()
* cleanUpResult()
* cleanUpAnagram()
* setupAnagram(scope, index)
* shuffleArray(input)
* stringInArray(input, what)
* initSlideshow(scope)
* decrementSlideIndex()
* incrementSlideIndex()
* showSlide(scope, index)
* initQuestion(scope, questionNumber)
* answerQuestion(scope, questionNumber, responseWasTrue)

 WWW_THEDIAMONDCASINOANDRESORT_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_THEDIAMONDCASINOANDRESORT_COM()
* INITIALISE(mc)
* initPages()
* initOptions()
* setPage(pageName, PageClass)
* POPULATE_TEXT(pageName, searchArgs, newPage)
* displayPage(pageName)
* TXD_HAS_LOADED(txd, success, id)
* DISABLE_VIDEO(isDisabled)
* CLEANUP()
* goToAnchor(link)
* handleLB()
* handleRB()
* handleLT()
* handleRT()
* handleLTRelease()
* handleRTRelease()
* handleAnalogStickInput(isLeftStick, x, y, isScrollWheel)
* handleMouseClick(inputIsMouseClick)
* handleMouseRelease()
* getPresetData(index)
* getSuiteBaseCost(getSaleCost)
* getMembershipCost(getSaleCost)
* getColourCosts(costSums)
* getColourCost(optionIndex, getSaleCost)
* getStyleCosts(costSums)
* getStyleCost(optionIndex, getSaleCost)
* getLoungeCosts(costSums)
* getBarCosts(costSums)
* getBarCost(optionIndex, getSaleCost)
* getDealerCosts(costSums)
* getBedroomCosts(costSums)
* getMediaRoomCosts(costSums)
* getSpaCosts(costSums)
* getOfficeCosts(costSums)
* getGarageCosts(costSums)
* getCost(costSums, offset)
* getRawCost(offset, sale)
* dispatchSuiteSelections()
* setPageHeight(height)

 WWW_THEINTERNETISAHELLHOLE_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_THEINTERNETISAHELLHOLE_COM()
* READY()
* POPULATE_TEXT(pageName)

 WWW_THEPOWCLEANSE_COM
^^^^^^^^^^^^^^^^^^^^^^

* WWW_THEPOWCLEANSE_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_THEREALITYMILL_COM
^^^^^^^^^^^^^^^^^^^^^^^

* WWW_THEREALITYMILL_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)
* displayPurchasedText()

 WWW_TOESHOESUSA_COM
^^^^^^^^^^^^^^^^^^^^

* WWW_TOESHOESUSA_COM()
* READY()
* POPULATE_TEXT(pageName)
* slideToNextImage()
* goToAnchor(AnchorLink)

 WWW_VINEWOODLOGLINEGENERATOR_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_VINEWOODLOGLINEGENERATOR_COM()
* READY()
* initGenerator()
* setNextSelectedGenCharacterFlawsId(direction)
* generatorFlawSelect(direction)
* generatorStrengthSelect(id)
* generatorCrisisSelect(id)
* generatorHeroSelect(direction)
* generatorSidekickSelect()
* generatorSpecialSelect(id)
* generatorAntagonistSelect(id)
* generatorGoalSelect(id)
* generateLogline()
* populateLogline()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_VISITTHEALAMOSEA_COM
^^^^^^^^^^^^^^^^^^^^^^^^^


 WWW_WARSTOCK_D_CACHE_D_AND_D_CARRY_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_WARSTOCK_D_CACHE_D_AND_D_CARRY_COM()
* INITIALISE(mc)
* TXD_HAS_LOADED(txd, success, id)
* CLEANUP()
* filterVehicles()
* setCommonPageIDs()
* updateBackground(contentItem, page)
* initStats(page)
* displayImage(vehicle, container)
* goToAnchor(link)
* displayPage(pageName)
* handleLB()
* handleRB()
* POPULATE_TEXT(pageName, searchArgs, newPage)
* showTruckPage(pageView, PageClass, type)
* showTruckPopup(message)
* hideTruckPopup()
* showChopperPage(pageView, PageClass, type)
* showHackerPage(pageView, PageClass, type)
* showSubPage(pageView, PageClass, type)
* getBasePrice()
* getBaseSalePrice()
* getBuyFromPrice()
* getBuyFromSalePrice()
* getCabCost(index)
* getCabSaleCost(index)
* getModuleCost(index)
* getModuleSaleCost(index)
* getColourCost(index)
* getColourSaleCost(index)
* initTruckDefaultSelections()
* dispatchPlayerTruckSelections()
* getChopperBasePrice()
* getChopperBaseSalePrice()
* getChopperBuyFromPrice()
* getChopperBuyFromSalePrice()
* getChopperTurretCost(index)
* getChopperTurretSaleCost(index)
* getChopperVehicleCost(index)
* getChopperVehicleSaleCost(index)
* getChopperWeaponCost(index)
* getChopperWeaponSaleCost(index)
* getChopperInteriorCost(index)
* getChopperInteriorSaleCost(index)
* initChopperDefaultSelections()
* dispatchPlayerChopperSelections()
* getHackerBasePrice()
* getHackerBaseSalePrice()
* getHackerBuyFromPrice()
* getHackerBuyFromSalePrice()
* getHackerMissileCost(index)
* getHackerMissileSaleCost(index)
* getHackerDroneCost(index)
* getHackerDroneSaleCost(index)
* getHackerWeaponCost(index)
* getHackerWeaponSaleCost(index)
* getHackerWorkshopCost(index)
* getHackerWorkshopSaleCost(index)
* getHackerTintCost(index)
* getHackerTintSaleCost(index)
* getHackerDecalCost(index)
* getHackerDecalSaleCost(index)
* initHackerDefaultSelections()
* dispatchPlayerHackerSelections()
* getSubBasePrice()
* getSubBaseSalePrice()
* getSubBuyFromPrice()
* getSubBuyFromSalePrice()
* getSubSonarCost(index)
* getSubSonarSaleCost(index)
* getSubMissilesCost(index)
* getSubMissilesSaleCost(index)
* getSubWorkshopCost(index)
* getSubWorkshopSaleCost(index)
* getSubHelicopterCost(index)
* getSubHelicopterSaleCost(index)
* getSubMiniSubCost(index)
* getSubMiniSubSaleCost(index)
* getSubColourCost(index)
* getSubColourSaleCost(index)
* getSubFlagCost(index)
* getSubFlagSaleCost(index)
* initSubDefaultSelections()
* dispatchPlayerSubSelections()
* getActiveButtonID()
* initHomePage(newPage)
* initTruckBanner(useSmallLayout, allowForSubBanner)
* initChopperBanner(useSmallLayout, allowForSubBanner)
* initHackerBanner(allowForSubBanner)
* initSubBanner()
* initDetailsPage(pageName, newPage)
* initBuyItNowDetailsPage(id, currentVehicle, newPage, frame)
* initOptions(page)
* initSelectedOption(page)
* setOptionsButtons(selectedOption)
* initVehicleButton(vehicle, container, x, y)
* initSuccessPage(newPage)
* initOutcomePage(headerText, bodyText, soldLabel)
* formatNumber(value)

 WWW_WARSTOCK_D_CACHE_D_AND_D_CARRY_COM_WRAPPER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_WARSTOCK_D_CACHE_D_AND_D_CARRY_COM_WRAPPER()

 WWW_WHOKILLEDLEONORAJOHNSON_COM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_WHOKILLEDLEONORAJOHNSON_COM()
* READY()
* POPULATE_TEXT(pageName)
* scan_and_set_localised_text(scope)

 WWW_YOURDEADFAMILY_COM
^^^^^^^^^^^^^^^^^^^^^^^

* WWW_YOURDEADFAMILY_COM()
* READY()
* goToAnchor(AnchorLink)
* POPULATE_TEXT(pageName)

 WWW_YOURNEWBABYSNAME_COM
^^^^^^^^^^^^^^^^^^^^^^^^^

* WWW_YOURNEWBABYSNAME_COM()
* READY()
* POPULATE_TEXT(pageName)
* goToAnchor(AnchorLink)
