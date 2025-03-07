<?php

declare(strict_types=1);

use Rector\Config\RectorConfig;
use Rector\Set\ValueObject\LevelSetList;
use Rector\Symfony\Set\SymfonyLevelSetList;
use Rector\Symfony\Set\SymfonySetList;

return static function (RectorConfig $rectorConfig): void {
  $rectorConfig->paths([
    __DIR__.'/src',
    __DIR__.'/config',
  ]);

  $rectorConfig->symfonyContainerXml(__DIR__.'/var/cache/dev/App_KernelDevDebugContainer.xml');

  $rectorConfig->sets([
    LevelSetList::UP_TO_PHP_82,
    //    SymfonyLevelSetList::UP_TO_SYMFONY_60,
    //    SymfonySetList::SYMFONY_CODE_QUALITY,
    //    SymfonySetList::SYMFONY_CONSTRUCTOR_INJECTION,
    \Rector\Set\ValueObject\SetList::DEAD_CODE,
  ]);

  $rectorConfig->skip([__DIR__.'/src/System/Testing/DataFixtures/DataBaseUtils.php']);
};
